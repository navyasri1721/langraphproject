import streamlit as st

from graph.graph_builder import build_graph

graph = build_graph()

st.set_page_config(
    page_title="IPL LangGraph RAG",
    layout="wide"
)

st.title("🏏 IPL LangGraph RAG Assistant")

# -------------------------
# Session State
# -------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------
# Sidebar
# -------------------------

st.sidebar.title("Knowledge Base")

dataset = st.sidebar.selectbox(
    "Choose Dataset",
    [
        "IPL Dataset",
        "Uploaded PDFs"
    ]
)

uploaded_files = st.sidebar.file_uploader(
    "Upload PDF Files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    st.sidebar.success(
        f"{len(uploaded_files)} file(s) selected"
    )

show_chunks = st.sidebar.checkbox(
    "Show Retrieved Chunks"
)

# -------------------------
# Chat History
# -------------------------

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------------
# User Input
# -------------------------

query = st.chat_input(
    "Ask a question..."
)

if query:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    with st.chat_message("user"):
        st.markdown(query)

    result = graph.invoke(
        {
            "user_query": query,
            "query_type": "",
            "entities": [],
            "retrieved_context": [],
            "context": "",
            "final_answer": ""
        }
    )
    st.write(result)
    answer = result["final_answer"]
    

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    if show_chunks:

        st.subheader("Retrieved Context")

        for i, chunk in enumerate(
            result.get(
                "retrieved_context",
                []
            ),
            start=1
        ):
            with st.expander(
                f"Chunk {i}"
            ):
                st.write(chunk)