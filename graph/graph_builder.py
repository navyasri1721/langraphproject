from langgraph.graph import StateGraph
from langgraph.graph import END

from graph.state import IPLAgentState

from graph.router import route_query

from graph.nodes.team_node import team_node
from graph.nodes.batting_node import batting_node
from graph.nodes.bowling_node import bowling_node
from graph.nodes.venue_node import venue_node
from graph.nodes.form_node import form_node
from graph.nodes.h2h_node import h2h_node
from graph.nodes.records_node import records_node
from graph.nodes.synthesis_node import synthesis_node
from graph.nodes.answer_node import answer_node


def build_graph():

    graph = StateGraph(IPLAgentState)

    graph.add_node("team", team_node)
    graph.add_node("answer", answer_node)
    graph.add_node("batting", batting_node)
    graph.add_node("bowling", bowling_node)
    graph.add_node("venue", venue_node)
    graph.add_node("form", form_node)
    graph.add_node("h2h", h2h_node)
    graph.add_node("records", records_node)

    graph.add_node("synthesis", synthesis_node)

    graph.set_conditional_entry_point(
        route_query,
        {
            "team": "team",
            "batting": "batting",
            "bowling": "bowling",
            "venue": "venue",
            "form": "form",
            "h2h": "h2h",
            "records": "records"
        }
    )

    graph.add_edge("team", "synthesis")
    graph.add_edge("batting", "synthesis")
    graph.add_edge("bowling", "synthesis")
    graph.add_edge("venue", "synthesis")
    graph.add_edge("form", "synthesis")
    graph.add_edge("h2h", "synthesis")
    graph.add_edge("synthesis", "answer")
    graph.add_edge("answer", END)

    return graph.compile()