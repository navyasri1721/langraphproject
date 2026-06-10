from retriever.retriever import retrieve_documents


def records_node(state):

    docs = retrieve_documents(state["user_query"])

    state["retrieved_context"] = [
        doc.page_content for doc in docs
    ]

    return state