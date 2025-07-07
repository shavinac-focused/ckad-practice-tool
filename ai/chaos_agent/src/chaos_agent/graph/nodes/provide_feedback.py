from chaos_agent.graph.state import GraphState

def provide_feedback(state: GraphState) -> GraphState:
    """Generate helpful feedback based on verification"""
    if state.is_challenge_solved:
        # This shouldn't happen as the routing should go to reset_cluster
        return state
    
    # Provide hints based on attempt count
    if state.challenge and state.challenge.hints:
        hint_index = min(state.attempt_count - 1, len(state.challenge.hints) - 1)
        feedback = f"""
        Don't give up! Here's a hint that might help:
        
        HINT #{state.attempt_count}: {state.challenge.hints[hint_index]}
        
        Try again and run the verification when you're ready.
        """
        print(feedback)
        
    # Ask if the user wants to continue or get a new challenge
    print("\nWould you like to:")
    print("1. Continue working on this challenge")
    print("2. Get a new challenge")
    print("3. Exit practice session")

    # TODO - interrupt to ask for human feedback
    # For now, we'll just set a placeholder feedback
    state.user_feedback = "exit"
    
    return state
