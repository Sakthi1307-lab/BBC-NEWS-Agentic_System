from agent import config
from agent.state import State

def pick_source(state: State)->str:
    """Decsisoon 1 - after router, pick source based on route bbc or web"""
    return state.get("router", "bbc")

def enough_evidence(state: State)->str:
    """Decision 2 - after grade, check if we have enough relevant documents to generate an answer"""
    if  len(state.get("documents", [])) >= config.MIN_RELEVANT_DOCS:
     return "generate"
    return "search_web"