from utils.chunking import load_pdf, chunk_documents
from retriever.embeddings import load_embeddings
from retriever.vector_store import create_vector_store


PDF_PATH = "data/IPL_LangGraph_RAG_Dataset.pdf"


# -----------------------------
# TEXT CLEANING
# -----------------------------
def clean_chunk(text: str) -> str:
    return text.replace("\n", " ").strip()


# -----------------------------
# QUALITY FILTER
# -----------------------------
def is_good_chunk(text: str) -> bool:
    text = text.strip()

    # remove very small noise
    if len(text) < 40:
        return False

    # remove evaluation / instruction / system metadata chunks
    bad_keywords = [
        "LangGraph Node",
        "Evaluation Query",
        "ID Query Level",
        "Out-of-corpus",
        "Out-of-scope",
        "Node(s)",
        "RAG Skill"
    ]

    if any(k in text for k in bad_keywords):
        return False

    # must contain IPL relevant signals
    good_keywords = [
        "MI", "CSK", "RCB", "KKR", "RR", "DC", "SRH", "GT",
        "Titles", "Champions", "Runner-up"
    ]

    return any(k in text for k in good_keywords)


# -----------------------------
# MAIN PIPELINE
# -----------------------------
def main():

    print("Loading PDF...")
    documents = load_pdf(PDF_PATH)
    print(f"Pages Loaded: {len(documents)}")

    print("Creating Chunks...")
    chunks = chunk_documents(documents)
    print(f"Chunks Created: {len(chunks)}")

    print("Cleaning & Filtering Chunks...")

    cleaned_chunks = []
    seen = set()

    for doc in chunks:
        text = clean_chunk(doc.page_content)

        # apply filter
        if not is_good_chunk(text):
            continue

        # remove duplicates
        if text in seen:
            continue

        seen.add(text)

        doc.page_content = text
        cleaned_chunks.append(doc)

    print(f"Clean Chunks: {len(cleaned_chunks)}")

    print("Loading Embeddings Model...")
    embeddings = load_embeddings()

    print("Creating ChromaDB...")
    create_vector_store(cleaned_chunks, embeddings)

    print("Vector Store Created Successfully 🚀")


if __name__ == "__main__":
    main()