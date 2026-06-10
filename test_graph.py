from graph.graph_builder import build_graph

graph = build_graph()

result = graph.invoke(
    {
        "user_query": "Who captains CSK in 2024?",
        "query_type": "",
        "entities": [],
        "retrieved_context": [],
        "context": "",
        "final_answer": ""
    }
)

print(result["final_answer"])