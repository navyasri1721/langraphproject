from retriever.retriever import retrieve_documents

query = "Chennai Super Kings captain"

docs = retrieve_documents(query)

for i, doc in enumerate(docs):
    print(f"\nDOC {i+1}")
    print(doc.metadata)
    print(doc.page_content[:500])
    print("-" * 50)