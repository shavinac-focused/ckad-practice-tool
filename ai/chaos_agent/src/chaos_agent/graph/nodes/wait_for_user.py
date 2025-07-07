from langgraph.types import interrupt
from chaos_agent.graph.state import GraphState

def wait_for_user(state: GraphState) -> GraphState:
    """Pause execution until user attempts to solve"""
    
    print(f"\n--- Attempt #{state.attempt_count} ---")
    print("The challenge is active. You can now interact with the Kubernetes cluster.")

    user_response = interrupt(
        {
            "task": "Type 'verify' when you're ready to check your solution: "
        }
    )

    print("--- User Response Received ---")
    print(user_response)

    return {
        "attempt_count": state.attempt_count + 1,
        "user_feedback": user_response
    }
