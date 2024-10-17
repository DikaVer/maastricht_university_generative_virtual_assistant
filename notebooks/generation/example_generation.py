import os
import time

# First we change the directory to the root directory of the project.
os.chdir(os.getcwd().replace("\\notebooks\\generation", ""))
print(os.getcwd())  # Check this field to see if the directory is correct.
from model.models import Agent

# vector search
param_vs = {
    "embed_name": "openai_parser",
    "param":
        {
            "search_type": "similarity",
            "search_kwargs": {
                "k": 10,
                # "score_threshold": None
            }
        }
}

# multi query
param_mq = {
    "param":
        {
            "llm_model": "openai",
            "temperature": 0,
            "top_p": None,
            "top_k": None,
            "frequency_penalty": None,
            "max_tokens": None
        }
}

param_google_reranker = {
    "param":
        {
            "k": 5,
        }
}

# Response LLM
param_response_llm = {
    "param": {

        "llm": {
            "llm_model": "openai",
            "temperature": 0.2,
            "top_p": None,
            "top_k": None,
            "frequency_penalty": None,
            "max_tokens": None
        },
        "shots": {
            "embed_name": "openai",
            "k": 2  # 0 means no shot
        }
    }
}

model_in = {
    "vector_search": param_vs,
    "multi_query": param_mq,
    "google_reranker": param_google_reranker,
    "response_llm": param_response_llm
}

agent = Agent(model_in, DEBUG=False)

query = "Tragically, I missed the final product and report examination this morning due to believing it was at 1pm instead of 11am. I do not have a good explanation for this as I remember checking the schedule several times and was confident that it would be at 1pm and by the time I realised, it was already 10:55. After rereading the rules and regulations I can not find what would happen in this case"
# query = "I wanted to ask you a question related to the project meetings and the pre-examination. Two days ago, I had a surgery on my toe in my home country and even though I got discharged, it is recommended to me to visit the hospital every day for monitoring and dressings for the next one or two weeks(depending on my physical condition). My question is, if I show proof about the surgery and the recovery, can I participate in the project meetings and in the pre-examination online instead of on site?"
# Take a timer
start = time.time()
result = agent.generate_response(query,
                                 multi_query=True,
                                 retrieve_type="vector_search",
                                 rerank_type="google_reranker",
                                 self_reflection=True
                                 )
end = time.time()
print("Time: ", end - start)

# print("Keys: ", result.keys())
print("Result: ", result['response'])
# %%
