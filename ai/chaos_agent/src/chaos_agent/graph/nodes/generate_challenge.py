from typing import List
from chaos_agent.graph.state import Challenge

def generate_challenge(llm, topics: List[str] = None, difficulty: str = "medium") -> Challenge:
    """Generate a CKAD challenge using LLM"""
    # Use LLM to generate challenge based on CKAD topics
    prompt = f"""
    Generate a Kubernetes challenge for CKAD practice with difficulty: {difficulty}.
    Topics to focus on: {', '.join(topics) if topics else 'any CKAD topic'}.
    
    The challenge should:
    1. Be realistic and similar to actual CKAD exam questions
    2. Involve debugging issues in a Kubernetes cluster
    3. Have a clear objective and solution
    
    Format your response as:
    TITLE: [brief title]
    DESCRIPTION: [detailed description of the challenge]
    TOPICS: [comma-separated list of Kubernetes topics involved]
    HINTS: [3 progressive hints that help solve the challenge]
    """
    
    # Call LLM and parse response
    # ...
