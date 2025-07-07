from langgraph.types import interrupt
from chaos_agent.graph.state import GraphState
from chaos_agent.tools.kubectl_wrapper import kubectl_exec

def reset_cluster(state: GraphState) -> GraphState:
    """Return cluster to baseline state"""
    print("\nResetting cluster to baseline state...")
    
    # For each resource in the baseline manifests, apply it to restore the original state
    for resource_key, manifest_yaml in state.baseline_manifests.items():
        try:
            # Write the manifest to a temporary file
            resource_type, resource_name = resource_key.split('/')
            print(f"Restoring {resource_type}/{resource_name}...")
            
            # Apply the manifest using kubectl apply
            # In a real implementation, you'd write to a temp file and apply it
            # For now, we'll simulate by using kubectl replace
            result = kubectl_exec(f"apply -f - << EOF\n{manifest_yaml}\nEOF", "practice-apps")
            print(f"Result: {result if result else 'Success'}")
            
        except Exception as e:
            print(f"Error restoring {resource_key}: {str(e)}")
    
    # Reset challenge state
    state.is_challenge_active = False
    state.is_challenge_solved = False
    state.mutations = []
    state.verification_steps = []
    state.challenge = None
    state.attempt_count = 0

    # Check state.user_feedback in case we were sent here from provide_feedback
    if (state.user_feedback == "exit"):
        return { "user_feedback": "exit" }

    # Ask if the user wants to continue with a new challenge
    user_response = interrupt(
        {
            "task": """Would you like to:
            1. Start a new challenge
            2. Exit practice session"""
        }
    )
    if ('1' in user_response):
        return { "user_feedback": "new_challenge" }
    elif ('2' in user_response):
        return { "user_feedback": "exit" }
    else:
        print("Unknown response. Assuming you want to exit.")
        return { "user_feedback": "exit" }
