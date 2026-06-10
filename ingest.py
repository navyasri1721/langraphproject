from utils.chunking import load_pdf, chunk_documents
from retriever.embeddings import load_embeddings
from retriever.vector_store import create_vector_store


PDF_PATH = "data/IPL_LangGraph_RAG_Dataset.pdf"


def clean_chunk(text: str) -> str:
    return text.replace("\n", " ").strip()


def main():

    print("Loading PDF...")
    documents = load_pdf(PDF_PATH)
    print(f"Pages Loaded: {len(documents)}")

    print("Creating Chunks...")
    chunks = chunk_documents(documents)
    print(f"Chunks Created: {len(chunks)}")

    print("Cleaning Chunks...")

    cleaned_chunks = []
    for doc in chunks:
        text = clean_chunk(doc.page_content)

        # FILTER 1: remove junk lines
        if "death." in text:
            continue

        # FILTER 2: remove very small garbage chunks
        if len(text) < 30:
            continue

        doc.page_content = text
        cleaned_chunks.append(doc)

    print(f"Clean Chunks: {len(cleaned_chunks)}")

    print("Loading Embeddings Model...")
    embeddings = load_embeddings()

    print("Creating ChromaDB...")
    create_vector_store(cleaned_chunks, embeddings)

    print("Vector Store Created Successfully")


if __name__ == "__main__":
    main()