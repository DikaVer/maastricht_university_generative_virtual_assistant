def print_reciprocal_rank_fusion_result(results):
    print("\n\nReciprocal Rank Fusion Result:")
    for i, result in enumerate(results):
        print(f"{i + 1}. {result[0]}")


def _print_param(model_class):
    """
    Print parameters of Large Language Model.
    """
    results = ""
    for key, value in model_class:
        if value is not None:
            # Key with capital letter
            key = key[0].upper() + key[1:]
            results += f"{key}: {value}\n"
    return results


def print_multi_query(agent):
    """
    Print parameters of multi query.
    """
    print(f"\nMulti Query Initialized" +
          "\nMulti Query Parameters:" +
          f"\nLLM Model: \n{_print_param(agent.multi_query.llm)}" +
          f"\nPrompt: \n{_print_param(agent.multi_query.prompt)}"
          )


def print_vector_search(agent):
    """
    Print parameters of vector search.
    """
    print(f"\nVector Search Initialized" +
          "\nVector Search Parameters:" +
          f"\nVector Database: {agent.retriever.tags[0]}" +
          f"\nEmbedding Model: {agent.retriever.tags[1]}" +
          f"\nSearch Parameters: \n{agent.retriever.search_kwargs}"
          )


def print_response_llm(agent):
    """
    Print parameters of response llm.
    """
    print(f"\nResponse LLM Initialized" +
          "\nResponse LLM Parameters:" +
          f"\nLLM Model: \n{_print_param(agent.response_llm.llm)}" +
          f"\nPrompt: \n{_print_param(agent.response_llm.prompt)}"
          )


def print_reranker(agent):
    print("\n\nReranker Initialized")
    print(agent.reranker_model)
    print(agent.reranker_tokenizer)
    print(f"\nNumber of Retrieve: {agent.num_retrieve}")


def print_llm_reranker(agent):
    print("\n\nLLM Reranker Initialized")
    print(agent.llm_reranker_model)
    print(agent.llm_reranker_tokenizer)
    print(f"\nNumber of Retrieve: {agent.num_retrieve}")
