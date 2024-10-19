from typing import List

import nltk
import numpy as np
import torch
from keybert import KeyBERT
from keybert.backend import BaseEmbedder
from keyphrase_vectorizers import KeyphraseCountVectorizer
from langchain.chains.llm import LLMChain
from langchain_core.documents.base import Document
from langchain_core.output_parsers import BaseOutputParser
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel, Field
from langchain_google_community.vertex_rank import VertexAIRank
from model.raw_data import documents
from model.utils.instructionPromt import *
from model.utils.printHelpers import *
from model.utils.utils import *
from nltk.corpus import stopwords
from transformers import AutoModelForSequenceClassification, AutoTokenizer, AutoModelForCausalLM

nltk.download('stopwords')


class Agent:

    def __init__(self,
                 models_in: dict,
                 DEBUG: bool = False
                 ):
        # Check if GPU is available
        self.DEBUG = DEBUG
        self.num_retrieve = None
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self._create_self_reflection()
        if self.DEBUG:
            print(f"Device: {self.device}")

        for key, value in models_in.items():
            if key == "vector_search":
                self._create_vector_search(value["embed_name"], value["param"])
                if self.DEBUG:
                    print_vector_search(self)
            elif key == "multi_query":
                self._create_multi_query(value["param"])
                if self.DEBUG:
                    print_multi_query(self)
            elif key == "keyword_extractor":
                self._create_keyword_extractor(value["embed_name"])
                if self.DEBUG:
                    pass
            elif key == "reranker":
                self._create_reranker(value["param"])
                if self.DEBUG:
                    print_reranker(self)
            elif key == "llm_reranker":
                self._create_llm_reranker(value["param"])
                if self.DEBUG:
                    print_llm_reranker(self)
            elif key == "response_llm":
                self._create_response_llm(value["param"])
                if self.DEBUG:
                    print_response_llm(self)
            elif key == "google_reranker":
                self._create_google_reranker(value["param"])
            else:
                raise ValueError(f"Model {key} not found. Please choose from 'vector_search', 'multi_query', "
                                 "'keyword_extractor', 'reranker' or 'llm_reranker'.")

    def generate_response(self,
                          query: str,
                          previous_queries: List[dict] = None,
                          multi_query: bool = True,
                          retrieve_type: str = "vector_search",  # vector_search, reranker, llm_reranker
                          rerank_type: str = "reranker",  # reranker, llm_reranker, google_reranker
                          self_reflection: bool = True
                          ):

        structured_steps = {}
        """
        Generate response based on query.
        """
        if retrieve_type == "llm_reranker" and rerank_type == "llm_reranker":
            raise ValueError("Both Retrieve Type and Rerank Type cannot be 'llm_reranker' at the same time.")
        elif retrieve_type == "reranker" and rerank_type == "reranker":
            raise ValueError("Both Retrieve Type and Rerank Type cannot be 'reranker' at the same time.")

        multi_context = None
        multi_queries = None
        response = ""
        attemptCount = 0
        isUsefull = False

        while not isUsefull:

            # Save the structured steps
            structured_steps[attemptCount] = {}
            structured_steps[attemptCount]["query"] = query

            # Multi-Query
            if multi_query:  # Generate multiple queries
                multi_queries = self.generate_multi_query(query)["text"]
                structured_steps[attemptCount]["multi_queries"] = multi_queries

            # Retrieve context based on query
            if "vector_search" == retrieve_type:
                # Retrieve context based on original query
                context = self.retrieve_content(query)

                # Retrieve context based on multiple queries
                if multi_query:
                    assert multi_queries is not None
                    multi_context = [self.retrieve_content(multi_query) for multi_query in multi_queries]
            elif "reranker" == retrieve_type:
                context = self.retrieve_content_with_reranker(query, top_n=self.num_retrieve)
                if multi_query:
                    assert multi_queries is not None
                    multi_context = [self.retrieve_content_with_reranker(multi_query, top_n=self.num_retrieve) for
                                     multi_query in multi_queries]
            elif "llm_reranker" == retrieve_type:
                context = self.retrieve_content_with_llm_reranker(query, top_n=self.num_retrieve)
                if multi_query:
                    assert multi_queries is not None
                    multi_context = [self.retrieve_content_with_llm_reranker(multi_query, top_n=self.num_retrieve) for
                                     multi_query in multi_queries]
            else:
                raise ValueError(
                    f"Retrieve Type {retrieve_type} not found. Please choose from 'vector_search', 'reranker' "
                    "or 'llm_reranker'.")

            if context is None:
                raise ValueError("Content not found. Please check the retrieval process.")

            if multi_query and multi_context is None:
                raise ValueError("Multi Content not found. Please check the retrieval process.")

            # Save the structured steps
            if multi_query:
                # Reciprocal Rank Fusion
                contents = [context] + multi_context
                context = self.apply_reciprocal_rank_fusion(contents, k=60)

            structured_steps[attemptCount]["context"] = context

            # Rerank the context
            if "reranker" == rerank_type:
                context = self.rerank_content(context, query, top_n=self.num_retrieve)
            elif "llm_reranker" == rerank_type:
                context = self.rerank_content_with_llm(context, query, top_n=self.num_retrieve)
            elif "google_reranker" == rerank_type:
                order = self.google_reranker.compress_documents(context, query)
                context = reorder_context(context, order)
            else:
                print("No reranker applied")

            structured_steps[attemptCount]["reranked_context"] = context

            # print(UnderstandModel().evaluate(context, query))
            # print(ClarificationModel().evaluate(context, query))
            # return None

            final_context = get_structured_context(context)

            if previous_queries:
                instruction = "<Previous Questions>\n"
                instruction += "\nThese are the previous queries, which can be helpful for answering the question:\n"
                for message in previous_queries:
                    if message.get('role') == "user":
                        instruction += f"human: {message.get('content')}\n"
                    else:
                        instruction += f"ai: {message.get('content')}\n"
                    previous_queries = instruction
                instruction += "</Previous Questions>\n"
            else:
                previous_queries = "<Previous Questions>\n</Previous Questions>"

            # Generate response based on the context
            if self_reflection:
                flag = True
                max_tries = 3
                while flag and max_tries >= 0:
                    response = self.response_llm({"query": query,
                                                  "context": final_context,
                                                  "input": query,  # For Shots
                                                  "prev_q": previous_queries
                                                  })["text"]

                    score = self.hallucination_grader.evaluate(context, response)
                    grade = score.binary_score
                    if grade == "yes":
                        flag = False
                    else:
                        max_tries -= 1

                if not flag:
                    structured_steps[attemptCount]["response"] = response
                else:
                    response = ClarificationModel().evaluate(context, query)
                    structured_steps[attemptCount]["response"] = response
                    break

                # Evaluate the response
                score = self.answer_grader.evaluate(query, response)
                grade = score.binary_score
                if grade == "yes":
                    # Save the structured steps
                    isUsefull = True
                    structured_steps[attemptCount]["isUsefull"] = isUsefull
                    if isUsefull:
                        break
                else:
                    query = self.rewrite_model.rewrite(query)
                    attemptCount += 1
                    if attemptCount > 1:
                        response = ClarificationModel().evaluate(context, query)
                        break
            else:
                response = self.response_llm({"query": query,
                                              "context": final_context,
                                              "input": query,  # For Shots
                                              "prev_q": previous_queries
                                              })["text"]
                break

        return {"context": structured_steps,
                "query": query,
                "response": response}

    def self_reflection(self, context: List[Document], generation: str, question: str):
        score = self.hallucination_grader.evaluate(context, generation)
        grade = score.binary_score
        if grade == "yes":
            score = self.answer_grader.evaluate(question, generation)
            grade = score.binary_score
            if grade == "yes":
                return True, None
            else:
                return False, "Answer does not address the question."
        else:
            return False, "Answer is not grounded in the facts."

    def embed_query(self, query: str):
        """
        Embed query using the vector store.
        """
        if self.vector_db is None:
            raise ValueError("Vector Store is not initialized. Create Agent with 'vector_search' key in models_in.")

        if isinstance(self.vector_db.embeddings, HuggingFaceHubEmbeddings):
            return self.vector_db.embeddings.embed_query(INSTRUCTION_BGE + query)
        else:
            return self.vector_db.embeddings.embed_query(query)

    def embed_documents(self, docs: list):
        """
        Embed documents using the vector store.
        """
        if self.vector_db is None:
            raise ValueError("Vector Store is not initialized. Create Agent with 'vector_search' key in models_in.")

        if isinstance(self.vector_db.embeddings, HuggingFaceHubEmbeddings):
            docs = [INSTRUCTION_BGE + doc for doc in docs]
            return self.vector_db.embeddings.embed_documents(docs)
        else:
            return self.vector_db.embeddings.embed_documents(docs)

    def retrieve_content(self, query: str):
        """
        Retrieve content based on query.
        """
        if self.retriever is None or self.vector_db is None:
            raise ValueError("Vector Search is not initialized. Create Agent with 'vector_search' key in models_in.")
        if isinstance(self.vector_db.embeddings, HuggingFaceHubEmbeddings):
            results = self.retriever.invoke(INSTRUCTION_BGE + query)
            if self.DEBUG:
                print("\n\nRetriever Results:")
                for i, result in enumerate(results):
                    print(f"{i + 1}. {result.page_content}")
            return results
        else:
            results = self.retriever.invoke(query)
            if self.DEBUG:
                print("\n\nRetriever Results:")
                for i, result in enumerate(results):
                    print(f"{i + 1}. {result.page_content}")
            return results

    def retrieve_content_with_reranker(self, query: str, top_n=5):
        """
        Retrieve content based on query and rerank the results.
        """
        if self.reranker_model is None or self.reranker_tokenizer is None:
            raise ValueError("Reranker is not initialized. Create Agent with 'reranker' key in models_in."
                             )
        pairs = [[query, doc.page_content] for doc in documents]
        with torch.no_grad():
            inputs = self.reranker_tokenizer(pairs, padding=True, truncation=True, return_tensors='pt',
                                             max_length=512).to(self.device)
            scores = self.reranker_model(**inputs, return_dict=True).logits.view(-1, ).float()

        # Return top_n documents based on scores
        top_n_indices = scores.argsort(descending=True)[:top_n]
        # From tensor to list
        top_n_indices = top_n_indices.cpu().numpy().tolist()

        results = [documents[i] for i in top_n_indices]

        if self.DEBUG:
            print("\n\nReranker Results:")
            for i, result in enumerate(results):
                print(f"{i + 1}. {result.page_content}")

        return results

    def retrieve_content_with_llm_reranker(self, query: str, top_n=5):
        """
        Retrieve content based on query and rerank the results with LLM.
        """
        if self.llm_reranker_model is None or self.llm_reranker_tokenizer is None:
            raise ValueError("LLM Reranker is not initialized. Create Agent with 'llm_reranker' key in models_in.")

        pairs = [[query, doc.page_content] for doc in documents]
        with torch.no_grad():
            inputs = get_inputs(pairs, self.llm_reranker_tokenizer, self.device)
            # batch the inputs with 16
            for i in range(0, inputs['input_ids'].size(0), 16):
                inputs_batch = {k: v[i:i + 16] for k, v in inputs.items()}
                scores = self.llm_reranker_model(**inputs_batch, return_dict=True).logits[:, -1, self.yes_loc].view(
                    -1, ).float()
                if i == 0:
                    all_scores = scores
                else:
                    all_scores = torch.cat((all_scores, scores), 0)

        # Return top_n documents based on scores
        top_n_indices = all_scores.argsort(descending=True)[:top_n]
        # From tensor to list
        top_n_indices = top_n_indices.cpu().numpy().tolist()

        results = [documents[i] for i in top_n_indices]

        if self.DEBUG:
            print("\n\nLLM Reranker Results:")
            for i, result in enumerate(results):
                print(f"{i + 1}. {result.page_content}")

        return results

    def rerank_content(self, context: List[Document], query: str, top_n: int = 5):
        """
        Rerank the content based on the query.
        """
        if self.reranker_model is None or self.reranker_tokenizer is None:
            raise ValueError("Reranker is not initialized. Create Agent with 'reranker' key in models_in.")

        pairs = [[query, doc.page_content] for doc in context]
        with torch.no_grad():
            inputs = self.reranker_tokenizer(pairs, padding=True, truncation=True, return_tensors='pt',
                                             max_length=512).to(self.device)
            scores = self.reranker_model(**inputs, return_dict=True).logits.view(-1, ).float()

        # Return top_n documents based on scores
        top_n_indices = scores.argsort(descending=True)[:top_n]
        # From tensor to list
        top_n_indices = top_n_indices.cpu().numpy().tolist()

        results = [context[i] for i in top_n_indices]

        if self.DEBUG:
            print("\n\nReranker content Results:")
            for i, result in enumerate(results):
                print(f"{i + 1}. {result.page_content}")

        return results

    def rerank_content_with_llm(self, context: List[Document], query: str, top_n: int = 5):
        """
        Rerank the content based on the query with LLM.
        """
        if self.llm_reranker_model is None or self.llm_reranker_tokenizer is None:
            raise ValueError("LLM Reranker is not initialized. Create Agent with 'llm_reranker' key in models_in.")

        pairs = [[query, doc.page_content] for doc in context]
        with torch.no_grad():
            inputs = get_inputs(pairs, self.llm_reranker_tokenizer, self.device)
            # batch the inputs with 16
            for i in range(0, inputs['input_ids'].size(0), 16):
                inputs_batch = {k: v[i:i + 16] for k, v in inputs.items()}
                scores = self.llm_reranker_model(**inputs_batch, return_dict=True).logits[:, -1, self.yes_loc].view(
                    -1, ).float()
                if i == 0:
                    all_scores = scores
                else:
                    all_scores = torch.cat((all_scores, scores), 0)

        # Return top_n documents based on scores
        top_n_indices = all_scores.argsort(descending=True)[:top_n]
        # From tensor to list
        top_n_indices = top_n_indices.cpu().numpy().tolist()

        results = [context[i] for i in top_n_indices]

        if self.DEBUG:
            print("\n\nLLM Reranker content Results:")
            for i, result in enumerate(results):
                print(f"{i + 1}. {result.page_content}")

        return results

    def extract_keywords(self, queries: str or List[str],
                         vectorizer=KeyphraseCountVectorizer(stop_words=stopwords.words('english')),
                         top_n=30
                         ):
        if isinstance(queries, str):
            queries = [queries]
        """
        Extract keywords from queries.
        """
        if self.keyword_extractor is None:
            raise ValueError("Keyword Extractor is not initialized. Create Agent with 'keyword_extractor' key in "
                             "models_in.")

        return self.keyword_extractor.extract_keywords(queries,
                                                       vectorizer=vectorizer,
                                                       top_n=top_n)

    def generate_multi_query(self, query: str):
        """
        Generate multiple queries based on the input query.
        """
        if self.multi_query is None:
            raise ValueError("Multi Query is not initialized. Create Agent with 'multi_query' key in models_in.")

        return self.multi_query({"question": query})

    def apply_reciprocal_rank_fusion(self,
                                     content: List[List[Document]],
                                     k: int = 60
                                     # Constant (But also can be used for assigning importance for retrievers)
                                     ):
        """
        Reciprocal Rank Fusion.
        """
        # Create a dictionary without repetition
        results = {}
        for query_retrieve in content:
            for passage in query_retrieve:
                if passage.page_content not in results:
                    results[passage.page_content] = {
                        "score": 0,
                        "original_document": passage
                    }

        # Apply Reciprocal Rank Fusion algorithm
        for query_retrieve in content:
            for passage in query_retrieve:
                results[passage.page_content]["score"] += 1 / (query_retrieve.index(passage) + k)

        # Sort the results based on the score
        sorted_results = sorted(results.items(), key=lambda x: x[1]["score"], reverse=True)

        # Print the top documents
        if self.DEBUG:
            print_reciprocal_rank_fusion_result(sorted_results)

        # Return the sorted results with original documents
        return [result[1]["original_document"] for result in sorted_results]

    def _create_vector_search(self, embed_name: str, param: dict):
        """
        Create vector search.
        """
        self.vector_db = get_vector_store(embed_name)
        self.retriever = self.vector_db.as_retriever(**param)

    def _create_multi_query(self, param: dict):
        """
        Create multi query.
        """
        llm_model = get_llm_model(**param)
        output_parser = LineListOutputParser()
        self.multi_query = LLMChain(llm=llm_model, prompt=DEFAULT_MULTI_QUERY_PROMPT, output_parser=output_parser)

    def _create_response_llm(self, param: dict):
        """
        Create multi query.
        """
        llm_model = get_llm_model(**param["llm"])
        prompt = get_instruction_generation_prompt(**param["shots"])
        self.response_llm = LLMChain(llm=llm_model, prompt=prompt)

    def _create_keyword_extractor(self, embed_name: str):
        """
        Create keyword extractor.
        """
        self.keyword_extractor = KeyBERT(model=CustomEmbedder(get_embed_model(embed_name)))

    def _create_reranker(self, param: dict):
        self.reranker_tokenizer = AutoTokenizer.from_pretrained('BAAI/bge-reranker-v2-m3')
        self.reranker_model = AutoModelForSequenceClassification.from_pretrained('BAAI/bge-reranker-v2-m3').to(
            self.device)
        self.reranker_model.eval()
        self.num_retrieve = param["k"]

    def _create_llm_reranker(self, param: dict):
        self.llm_reranker_tokenizer = AutoTokenizer.from_pretrained('BAAI/bge-reranker-v2-gemma')
        self.llm_reranker_model = AutoModelForCausalLM.from_pretrained('BAAI/bge-reranker-v2-gemma').to(self.device)
        self.yes_loc = self.llm_reranker_tokenizer('Yes', add_special_tokens=False)['input_ids'][0]
        self.llm_reranker_model.eval()
        self.num_retrieve = param["k"]

    def _create_google_reranker(self, param: dict):
        self.google_reranker = VertexAIRank(
            project_id=Config.GOOGLE_PROJECT_ID,
            location_id="global",
            ranking_config="default_ranking_config",
            title_field="source",
            top_n=param["k"],
        )

    def _create_self_reflection(self):
        self.hallucination_grader = HallucinationsModel()
        self.answer_grader = GradeModel()
        self.rewrite_model = RewriteModel()


# class UnderstandQuestion(BaseModel):
#     """Binary score for hallucination present in generation answer."""
#
#     binary_score: str = Field(
#         description="Question is clear, 'yes' or 'no'"
#     )
#
#
# class UnderstandModel:
#     def __init__(self):
#         # LLM with function call
#         llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0, openai_api_key=Config.OPENAI_API_KEY)
#         structured_llm_grader = llm.with_structured_output(UnderstandQuestion)
#         # Prompt
#         system = """You are a understander assessing whether an user question is defined clearly.\n
#         Give a binary score 'yes' or 'no'. 'Yes' means that you do not need to ask for clarification to retrieve relevant documents from a vector database."""
#         understand_prompt = ChatPromptTemplate.from_messages(
#             [
#                 ("system", system),
#                 ("human", "User: \n\n {query}"),
#             ]
#         )
#         self.understand_grader = understand_prompt | structured_llm_grader
#
#     def evaluate(self, query: str):
#         return self.understand_grader.invoke({"query": query})


class ClarificationModel:
    def __init__(self):
        # LLM with function call
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, openai_api_key=Config.OPENAI_API_KEY)
        # Prompt
        system = (
                "You are a clarification model. Your task is to generate questions of the given user "
                "question and context to understand better his question." +
                "By generating multiple clarification perspectives on the user question and context," +
                "your goal is to help the user overcome some of the limitations" +
                "of distance-based similarity search, without asking additional information. Provide these alternative" +
                "questions separated by newlines. \n "
        )
        clarification_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system),
                ("human", "Set of context: \n\n {context} \n\n User: \n\n {query} \n\n Clarification questions:"),
            ]
        )
        # self.clarification_grader = clarification_prompt | llm | LineListOutputParser()
        self.clarification_grader = clarification_prompt | llm

    def evaluate(self, context: List[Document], query: str):
        return self.clarification_grader.invoke({"query": query, "context": get_context(context)})


class GradeHallucinations(BaseModel):
    """Binary score for hallucination present in generation answer."""

    binary_score: str = Field(
        description="Answer is grounded in the facts, 'yes' or 'no'"
    )


class HallucinationsModel:
    def __init__(self):
        # LLM with function call
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, openai_api_key=Config.OPENAI_API_KEY)
        structured_llm_grader = llm.with_structured_output(GradeHallucinations)
        # Prompt
        system = """You are a grader assessing whether an LLM generation is grounded in / supported by a set of retrieved facts. \n 
             Give a binary score 'yes' or 'no'. 'Yes' means that the answer is grounded in / supported by the set of facts."""
        hallucination_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system),
                ("human", "Set of facts: \n\n {documents} \n\n LLM generation: {generation}"),
            ]
        )
        self.hallucination_grader = hallucination_prompt | structured_llm_grader

    def evaluate(self, context: List[Document], generation: str):
        return self.hallucination_grader.invoke({"documents": get_context(context), "generation": generation})


class GradeAnswer(BaseModel):
    """Binary score to assess answer addresses question."""

    binary_score: str = Field(
        description="Answer addresses the question, 'yes' or 'no'"
    )


class GradeModel:
    def __init__(self):
        # LLM with function call
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, openai_api_key=Config.OPENAI_API_KEY)
        structured_llm_grader = llm.with_structured_output(GradeAnswer)
        system = """You are a grader assessing whether an answer addresses / resolves a question \n 
        Give a binary score 'yes' or 'no'. Yes' means that the answer resolves the question."""
        answer_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system),
                ("human", "User question: \n\n {question} \n\n LLM generation: {generation}"),
            ]
        )

        self.answer_grader = answer_prompt | structured_llm_grader

    def evaluate(self, question: str, generation: str):
        return self.answer_grader.invoke({"question": question, "generation": generation})


class RewriteModel:
    def __init__(self):
        # LLM with function call
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, openai_api_key=Config.OPENAI_API_KEY)
        system = """You are question re-writer that converts an input question to a better version that is optimized \n 
     for vectorstore retrieval. Look at the input and try to reason about the underlying semantic intent / meaning."""
        re_write_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system),
                (
                    "human",
                    "Here is the initial question: \n\n {question} \n Formulate an improved question.",
                ),
            ]
        )

        self.question_rewriter = re_write_prompt | llm | StrOutputParser()

    def rewrite(self, question: str):
        return self.question_rewriter.invoke({"question": question})


class LineListOutputParser(BaseOutputParser[List[str]]):
    """Output parser for a list of lines."""

    def parse(self, text: str) -> List[str]:
        lines = text.strip().split("\n")
        return lines


class CustomEmbedder(BaseEmbedder):
    def __init__(self, embedding_model):
        super().__init__()
        self.embedding_model = embedding_model

    def embed(self, documents, verbose=False):
        embeddings = self.embedding_model.embed_documents(documents)
        return np.array(embeddings)
