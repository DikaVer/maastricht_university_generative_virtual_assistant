import pickle

from langchain_chroma import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
)
from langchain_core.prompts.prompt import PromptTemplate
from model.utils.utils import get_embed_model
from tqdm.auto import tqdm

DEFAULT_MULTI_QUERY_PROMPT = PromptTemplate(
    input_variables=["question"],
    template="""
You are an AI language model assistant. Your task is to generate 3 different versions of the given user 
question to retrieve relevant documents from a vector database.
By generating multiple perspectives on the user question,
your goal is to help the user overcome some of the limitations
of distance-based similarity search. Provide these alternative
questions separated by newlines.
Original question: {question}
"""
)


def get_instruction_generation_prompt(embed_name: str = "openai",
                                      k: int = 2
                                      ):
    default_prompt = PromptTemplate(
        input_variables=["query", "context", "prev_q"],
        template="""Use the following pieces of context to answer the question at the end. If you don't know the 
        answer, just say that you don't know, don't try to make up an answer. Always give references to the generated 
        answer (document_name/article/page, e.g. "Reference: Rules and Regulation /article: 5.1.1 /page: 20.) along 
        with the provided information, there can be multiple references. Additionally, try to avoid contact with Board of Examiners 
        (BoE), and if you have to, make sure to suggest first contact the project coordinator.

    {prev_q}
    
    <Context>
    {context}
    </Context>
    
    <Question>
    {query}
    </Question>
    
    Use all context to generate a helpful, detailed and structured response with references.
    Helpful Answer:
        """,
    )

    if k > 0:
        # Get from pickle file
        with open("data/ShotDB/examplesQA.pkl", "rb") as f:
            examples = pickle.load(f)

        embedder_model = get_embed_model(embed_name)

        example_selector = SemanticSimilarityExampleSelector.from_examples(
            # This is the list of examples available to select from.
            examples,
            # This is the embedding class used to produce embeddings which are used to measure semantic similarity.
            embedder_model,
            # This is the VectorStore class that is used to store the embeddings and do a similarity search over.
            Chroma,
            # This is the number of examples to produce.
            k=k,
        )

        example_prompt = ChatPromptTemplate.from_messages(
            [
                ("human", "{input}"),
                ("ai", "{output}"),
            ]
        )
        few_shot_prompt = FewShotChatMessagePromptTemplate(
            example_prompt=example_prompt,
            example_selector=example_selector,
            input_variables=["input"]
        )

        return ChatPromptTemplate.from_messages(
            [
                ("system",
                 "You are an AI language model assistant. Your task is to generate a helpful response to the user query based on provided context."),
                few_shot_prompt,
                ("human", default_prompt.template),
            ]
        )
    else:
        return ChatPromptTemplate.from_messages(
            [
                ("system",
                 "You are an AI language model assistant. Your task is to generate a helpful response to the user query based on provided context."),
                ("human", default_prompt.template),
            ]
        )


INSTRUCTION_BGE = "Represent this sentence for searching relevant passages: "


def get_structured_context(context):
    final_context = ""
    for i, result in enumerate(context):
        final_context += str(i + 1) + ". " + result.page_content + " Reference: " + result.metadata['document_name']
        if 'article_name' in result.metadata:
            final_context += " /article: " + result.metadata['article_name']
        if 'page' in result.metadata:
            final_context += " /page: " + str(result.metadata['page']) + ".\n\n"

    return final_context


def get_context(context):
    final_context = ""
    for i, result in enumerate(context):
        final_context += (str(i + 1) + ". " + result.page_content + "\n\n")
    return final_context


def reorder_context(context, order):
    new_context = []
    for documents in order:
        new_context.append(context[int(documents.metadata["id"])])
    return new_context


def get_inputs(pairs, tokenizer, device, prompt=None, max_length=1024):
    if prompt is None:
        prompt = ("Given a query A and a passage B, determine whether the passage contains an answer to the query by "
                  "providing a prediction of either 'Yes' or 'No'.")
    sep = "\n"
    prompt_inputs = tokenizer(prompt,
                              return_tensors=None,
                              add_special_tokens=False)['input_ids']
    sep_inputs = tokenizer(sep,
                           return_tensors=None,
                           add_special_tokens=False)['input_ids']
    inputs = []
    progress_bar = tqdm(range(len(pairs)))
    for query, passage in pairs:
        query_inputs = tokenizer(f'A: {query}',
                                 return_tensors=None,
                                 add_special_tokens=False,
                                 max_length=max_length * 3 // 4,
                                 truncation=True)
        passage_inputs = tokenizer(f'B: {passage}',
                                   return_tensors=None,
                                   add_special_tokens=False,
                                   max_length=max_length,
                                   truncation=True)
        item = tokenizer.prepare_for_model(
            [tokenizer.bos_token_id] + query_inputs['input_ids'],
            sep_inputs + passage_inputs['input_ids'],
            truncation='only_second',
            max_length=max_length,
            padding=False,
            return_attention_mask=False,
            return_token_type_ids=False,
            add_special_tokens=False
        )
        item['input_ids'] = item['input_ids'] + sep_inputs + prompt_inputs
        item['attention_mask'] = [1] * len(item['input_ids'])
        inputs.append(item)
        progress_bar.update(1)

    return tokenizer.pad(
        inputs,
        padding=True,
        max_length=max_length + len(sep_inputs) + len(prompt_inputs),
        pad_to_multiple_of=8,
        return_tensors='pt',
    ).to(device)

# %%
