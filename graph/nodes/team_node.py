from retriever.retriever import retrieve_documents


def team_node(state):
    print("Executing Team Node")

    docs = retrieve_documents(state["user_query"])

    print("\n--- RETRIEVED DOCUMENTS ---\n")

    for i, doc in enumerate(docs):
        print(f"DOC {i+1}")
        print(doc.page_content)
        print("-" * 50)

    state["retrieved_context"] = [doc.page_content for doc in docs]

    return state
