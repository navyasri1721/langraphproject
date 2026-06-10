from retriever.embeddings import load_embeddings
from retriever.vector_store import load_vector_store

def get_retriever():

    embeddings = load_embeddings()

    vector_store = load_vector_store(embeddings)

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}
    )

    return retriever


def retrieve_documents(query):

    retriever = get_retriever()

    docs = retriever.invoke(query)

    return docs