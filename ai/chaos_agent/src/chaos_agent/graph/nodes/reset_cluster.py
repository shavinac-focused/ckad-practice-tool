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
    
    # Ask if the user wants to continue with a new challenge
    print("\nWould you like to:")
    print("1. Start a new challenge")
    print("2. Exit practice session")
    
    # In a real implementation, this would be handled by your UI/CLI
    # For now, we'll just set a placeholder feedback
    state.user_feedback = "new_challenge"
    
    return state
