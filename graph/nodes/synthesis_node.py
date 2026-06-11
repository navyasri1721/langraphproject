def synthesis_node(state):
    print("Executing Synthesis Node")

    docs = state["retrieved_context"]

    cleaned = [
        d for d in docs
        if len(d.strip()) > 20
    ]

    state["context"] = "\n\n".join(cleaned)

    return state