import time
from chaos_agent.graph.state import GraphState
from chaos_agent.tools.kubectl_wrapper import kubectl_exec

def apply_mutations(state: GraphState) -> GraphState:
    """Execute kubectl commands to apply mutations to the cluster"""
    if not state.mutations:
        print("No mutations to apply")
        return state
    
    # Record start time for the challenge
    state.start_time = time.time()
    state.is_challenge_active = True
    state.is_challenge_solved = False
    
    # Apply each mutation
    for i, mutation in enumerate(state.mutations):
        try:
            print(f"Applying mutation {i+1}/{len(state.mutations)}: {mutation.description}")
            print(f"(namespace: {mutation.namespace}) {mutation.kubectl_command}")
            result = kubectl_exec(mutation.kubectl_command, mutation.namespace)
            mutation.applied = True
            print(f"Result: {result if result else 'Success'}")
        except Exception as e:
            print(f"Error applying mutation: {str(e)}")
    
    return state
