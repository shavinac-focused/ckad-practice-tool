from langgraph.types import interrupt
from chaos_agent.graph.state import GraphState

def wait_for_user(state: GraphState) -> GraphState:
    """Pause execution until user attempts to solve"""
    attempts = state.attempt_count + 1
    
    print(f"\n--- Attempt #{attempts} ---")
    print("The challenge is active. You can now interact with the Kubernetes cluster.")

    user_response = interrupt(
        {
            "task": "Type 'verify' when you're ready to check your solution: "
        }
    )

    print("--- User Response Received ---")
    print(user_response)

    return {
        "attempt_count": attempts,
        "user_feedback": user_response
    }

# TODO - future extensions
# - Integrate with a web interface
# - Track start/stop time metrics
# - Allow asking for hints
# if user_input.lower() == 'hint' and state.challenge and state.challenge.hints:
#     hint_index = min(state.attempt_count - 1, len(state.challenge.hints) - 1)
#     print(f"HINT: {state.challenge.hints[hint_index]}")
