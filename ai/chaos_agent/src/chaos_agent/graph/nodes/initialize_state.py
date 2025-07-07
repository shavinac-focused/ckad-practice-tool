import yaml
from chaos_agent.graph.state import GraphState
from chaos_agent.tools.kubectl_wrapper import kubectl_exec

def initialize_state(state: GraphState) -> GraphState:
    """Set up initial graph state with baseline manifests"""
    # Get all resources in the practice-apps namespace
    resources_to_capture = [
        "deployments",
        "services",
        "configmaps",
        "secrets",
        "pods",
        "ingresses"
    ]
    
    baseline_manifests = {}
    
    for resource_type in resources_to_capture:
        try:
            # Get resources in YAML format
            result = kubectl_exec(f"get {resource_type} -o yaml")
            if result:
                # Parse the YAML to extract individual resources
                resources = yaml.safe_load(result)
                if resources and "items" in resources:
                    for item in resources["items"]:
                        name = item["metadata"]["name"]
                        key = f"{resource_type}/{name}"
                        baseline_manifests[key] = yaml.dump(item)
        except Exception as e:
            print(f"Error capturing baseline for {resource_type}: {str(e)}")
    
    # Reset state metrics
    state.baseline_manifests = baseline_manifests
    state.is_challenge_active = False
    state.is_challenge_solved = False
    state.attempt_count = 0
    state.user_feedback = None
    state.start_time = None
    state.solve_time = None
    
    return state
