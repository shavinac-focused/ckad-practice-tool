
from typing import List
from chaos_agent.graph.state import Mutation, VerificationStep
from chaos_agent.tools.kubectl_wrapper import kubectl_exec


def verify_solution(mutations: List[Mutation], verification_steps: List[VerificationStep]) -> bool:
    """Verify if the user has fixed all the issues"""
    for step in verification_steps:
        result = kubectl_exec(step.command)
        if step.expected_output not in result:
            return False
    return True
