from retriever.embeddings import load_embeddings
from retriever.vector_store import load_vector_store

def get_retriever():

    embeddings = load_embeddings()

    vector_store = load_vector_store(embeddings)

    retriever = vector_store.as_retriever(
    search_type="mmr",   # IMPORTANT (not similarity)
    search_kwargs={
        "k": 3,
        "fetch_k": 10,
        "lambda_mult": 0.7,
        "filter": {"source": "data/IPL_LangGraph_RAG_Dataset.pdf"}
    }
)
    return retriever


def retrieve_documents(query):

    retriever = get_retriever()

    docs = retriever.invoke(query)

    return docs