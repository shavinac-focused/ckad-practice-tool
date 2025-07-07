import time
from chaos_agent.graph.state import GraphState
from chaos_agent.tools.kubectl_wrapper import kubectl_exec

def verify_solution(state: GraphState):
    """Check if user has fixed the issues"""
    if not state.verification_steps:
        print("No verification steps defined")
        return state
    
    all_passed = True
    for step in state.verification_steps:
        try:
            result = kubectl_exec(step.command, "practice-apps")
            passed = step.expected_output in result
            print(f"Verification step: {step.description} - {'PASSED' if passed else 'FAILED'}")
            if not passed:
                all_passed = False
        except Exception as e:
            print(f"Error during verification: {str(e)}")
            all_passed = False
    
    if all_passed:
        solve_time = time.time() - (state.start_time or time.time())
        print(f"\n🎉 Congratulations! You've solved the challenge in {solve_time:.1f} seconds!")
        return {
            "is_challenge_solved": True,
            "solve_time": solve_time
        }
    else:
        print("\n❌ Not all verification steps passed. Keep trying!")
    
    return {
        "is_challenge_solved": False
    }
