from chaos_agent.graph.state import GraphState

def present_challenge(state: GraphState) -> GraphState:
    """Format challenge for user presentation"""
    if not state.challenge:
        print("No challenge to present")
        return state
    
    # Format the challenge for presentation
    challenge_text = f"""
    ===== CKAD PRACTICE CHALLENGE =====
    
    TITLE: {state.challenge.title}
    
    DESCRIPTION:
    {state.challenge.description}
    
    TOPICS: {', '.join(state.challenge.topics)}
    DIFFICULTY: {state.challenge.difficulty}
    
    ===================================
    
    Your task is to identify and fix the issues in the Kubernetes cluster.
    Type 'verify' when you think you've fixed the issues.
    """
    
    print(challenge_text)
    
    return state
