from typing import Literal
from langgraph.graph import START, END, StateGraph
from langgraph.checkpoint.memory import InMemorySaver
from chaos_agent.graph.state import GraphState
from chaos_agent.graph.nodes.initialize_state import initialize_state
from chaos_agent.graph.nodes.generate_challenge import generate_challenge
from chaos_agent.graph.nodes.design_mutations import design_mutations
from chaos_agent.graph.nodes.apply_mutations import apply_mutations
from chaos_agent.graph.nodes.present_challenge import present_challenge
from chaos_agent.graph.nodes.wait_for_user import wait_for_user
from chaos_agent.graph.nodes.verify_solution import verify_solution
from chaos_agent.graph.nodes.provide_feedback import provide_feedback
from chaos_agent.graph.nodes.reset_cluster import reset_cluster

def build_graph():
  builder = StateGraph(GraphState)

  # Add nodes to the graph
  builder.add_sequence([
    initialize_state,
    generate_challenge,
    design_mutations,
    apply_mutations,
    present_challenge,
    wait_for_user,
    verify_solution,
  ])
  builder.add_node(provide_feedback)
  builder.add_node(reset_cluster)

  # Add edges
  builder.add_edge(START, "initialize_state")
  builder.add_conditional_edges("verify_solution", route_on_solution_solved, ["reset_cluster", "provide_feedback"])
  builder.add_conditional_edges("reset_cluster", route_end_or_new_solution, ["generate_challenge", END])

  checkpointer = InMemorySaver()
  graph = builder.compile(checkpointer=checkpointer)
  print("--- Graph compiled successfully ---")

  return graph

def route_on_solution_solved(state: GraphState) -> Literal["reset_cluster", "provide_feedback"]:
  if state.is_challenge_solved:
    return "reset_cluster"
  return "provide_feedback"

def route_end_or_new_solution(state: GraphState) -> Literal["generate_challenge", "__end__"]:
  if state.user_feedback and state.user_feedback.lower() in ["quit", "exit", "end", "stop", "done"]:
    return END
  return "generate_challenge"
