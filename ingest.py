from utils.chunking import load_pdf, chunk_documents
from retriever.embeddings import get_embeddings
from retriever.vector_store import create_vector_store


PDF_PATH = "data/IPL_LangGraph_RAG_Dataset.pdf"


def main():

    print("Loading PDF...")

    documents = load_pdf(PDF_PATH)

    print(f"Pages Loaded: {len(documents)}")

    print("Creating Chunks...")

    chunks = chunk_documents(documents)

    print(f"Chunks Created: {len(chunks)}")

    print("Loading Embeddings Model...")

    embeddings = get_embeddings()

    print("Creating ChromaDB...")

    create_vector_store(chunks, embeddings)

    print("Vector Store Created Successfully")


if __name__ == "__main__":
    main()