from langgraph.graph import START, StateGraph, END

from agent.state import State
from agent.node import router,grade, search_bbc,search_web_doc,generate
from agent.routing import pick_source,enough_evidence

def build_graph():

    graph=StateGraph(State)

    graph.add_node("router", router)
    graph.add_node("search_bbc", search_bbc)
    graph.add_node("search_web_doc",search_web_doc)
    graph.add_node("grade", grade)
    graph.add_node("generate",generate)

    graph.add_edge(START,"router")
    graph.add_conditional_edges("router", pick_source,{"bbc":"search_bbc","web":"search_web_doc"})
    graph.add_edge("search_bbc","grade")
    graph.add_conditional_edges("grade",enough_evidence,{"generate":"generate","search_web":"search_web_doc"})
    graph.add_edge("search_web_doc", "grade")
    graph.add_edge("generate",END)

    return graph.compile()

