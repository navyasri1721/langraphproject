from retriever.retriever import retrieve_documents

query = "Who captains CSK in 2024?"

docs = retrieve_documents(query)

for doc in docs:
    print(doc.page_content)
    print("-" * 50)