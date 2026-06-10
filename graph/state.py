from typing import TypedDict, List

class IPLAgentState(TypedDict):
    user_query: str
    query_type: str
    entities: List[str]

    retrieved_context: List[str]

    context: str

    final_answer: str