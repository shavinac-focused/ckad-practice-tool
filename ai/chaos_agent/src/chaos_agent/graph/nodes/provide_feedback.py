from typing import Literal
from langgraph.types import interrupt, Command
from chaos_agent.graph.state import GraphState

def provide_feedback(state: GraphState) -> Command[Literal["wait_for_user", "reset_cluster", "__end__"]]:
    """Generate helpful feedback based on verification"""
    if state.is_challenge_solved:
        # This shouldn't happen as the routing should go to reset_cluster
        return Command(
            update={ "user_feedback": "" },
            goto="reset_cluster"
        )

    user_response = interrupt(
        {
            "task": """What would you like to do?
            1. Get a hint and continue working on this challenge
            2. Get a new challenge
            3. Exit practice session"""
        }
    )
    if ('1' in user_response):
        # Provide hints based on attempt count
        if state.challenge and state.challenge.hints:
            hint_index = min(state.attempt_count - 1, len(state.challenge.hints) - 1)
            feedback = f"""
            Don't give up! Here's a hint that might help:
            
            HINT #{hint_index + 1}: {state.challenge.hints[hint_index]}
            
            Try again and run the verification when you're ready.
            """
            print(feedback)

        return Command(
            update={ "user_feedback": "continue" },
            goto="wait_for_user"
        )
    elif ('2' in user_response):
        return Command(
            update={ "user_feedback": "new_challenge" },
            goto="reset_cluster"
        )
    elif ('3' in user_response):
        return Command(
            update={ "user_feedback": "exit" },
            goto="reset_cluster"
        )
    else:
        print("Unknown response. Assuming you want to exit.")
        return Command(
            update={ "user_feedback": "exit" },
            goto="reset_cluster"
        )
