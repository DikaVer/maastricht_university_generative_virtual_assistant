from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceHubEmbeddings
from langchain_google_vertexai import ChatVertexAI
from langchain_google_vertexai import VertexAIEmbeddings
from langchain_mistralai import MistralAIEmbeddings
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

# Load Environment Variables
load_dotenv()
from model.config import Config


def get_embed_model(embed_model
                    ):
    if "openai" == embed_model:
        return OpenAIEmbeddings(model="text-embedding-3-large",
                                openai_api_key=Config.OPENAI_API_KEY)
    elif "mistral" == embed_model:
        return MistralAIEmbeddings(api_key=Config.MISTRAL_API_KEY)
    elif "google" == embed_model:
        return VertexAIEmbeddings(model_name="textembedding-gecko@003",
                                  project=Config.GOOGLE_PROJECT_ID)
    elif "bge" == embed_model:
        return HuggingFaceHubEmbeddings(model='BAAI/bge-large-en-v1.5',
                                        task="feature-extraction",
                                        huggingfacehub_api_token=Config.HUGGINGFACE_API_KEY)
    else:
        raise ValueError(
            f"Embedding Model {embed_model} not found. Please choose from 'openai', 'mistral', 'google' "
            f"or 'bge'.")


def get_vector_store(vb_name
                     ):
    if "mistral" == vb_name:
        return Chroma(persist_directory="./data/vectorDB/mistral_vectorDB",
                      embedding_function=get_embed_model(vb_name))
    elif "openai" == vb_name:
        return Chroma(persist_directory="./data/vectorDB/openai_vectorDB",
                      embedding_function=get_embed_model(vb_name))
    elif "google" == vb_name:
        return Chroma(persist_directory="./data/vectorDB/google_vectorDB",
                      embedding_function=get_embed_model(vb_name))
    elif "bge" == vb_name:
        return Chroma(persist_directory="./data/vectorDB/bge_vectorDB", embedding_function=get_embed_model(vb_name))
    elif "openai_parser" == vb_name:
        return Chroma(persist_directory="./data/vectorDB/openai_vectorDB_google_parser",
                      embedding_function=get_embed_model("openai"))
    else:
        raise ValueError(
            f"Vector Store {vb_name} not found. Please choose from 'mistral', 'openai', 'google', 'bge' or 'openai_parser'.")


def get_llm_model(llm_model,
                  temperature: float = 0.3,
                  top_p: float = None,
                  top_k: int = None,
                  frequency_penalty: float = None,
                  max_tokens: int = None,
                  ):
    if "openai" == llm_model:
        if top_k is not None:
            # Print a warning message
            print("Warning: top_k is not supported in OpenAI models. Ignoring the parameter.")
        return ChatOpenAI(model="gpt-3.5-turbo-0125",
                          temperature=temperature,
                          max_tokens=max_tokens,
                          model_kwargs={
                              "top_p": top_p,
                              "frequency_penalty": frequency_penalty,
                          },
                          openai_api_key=Config.OPENAI_API_KEY
                          )
    elif "mistral" == llm_model:
        return ChatMistralAI(model="mistral-small-latest",
                             temperature=temperature,
                             top_p=top_p,
                             max_tokens=max_tokens,
                             model_kwargs={
                                 "frequency_penalty": frequency_penalty,
                                 "top_k": top_k,
                             },
                             mistral_api_key=Config.MISTRAL_API_KEY
                             )
    elif "google" == llm_model:
        return ChatVertexAI(model_name="gemini-1.0-pro",
                            temperature=temperature,
                            max_output_tokens=max_tokens,
                            top_p=top_p,
                            frequency_penalty=frequency_penalty,
                            top_k=top_k,
                            project=Config.GOOGLE_PROJECT_ID
                            )
    else:
        raise ValueError(f"Large Language Model {llm_model} not found. Please choose from 'openai', 'mistral', "
                         f"'google' or 'claude'.")
