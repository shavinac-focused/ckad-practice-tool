from chaos_agent.graph.state import GraphState
from langgraph.graph import StateGraph


def build_graph():
  builder = StateGraph(GraphState)

  graph = builder.compile()
  print("--- Graph compiled successfully ---")  # DEBUG

  return graph
