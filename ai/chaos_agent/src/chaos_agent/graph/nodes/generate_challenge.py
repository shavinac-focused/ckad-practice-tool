from chaos_agent.graph.state import Challenge, GraphState
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import json

load_dotenv()

def generate_challenge(state: GraphState) -> GraphState:
    """Generate a CKAD challenge using LLM"""

    difficulty = "medium"
    topics = ["pods", "deployments", "services"]
    prompt = f"""
    Generate a Kubernetes challenge for CKAD practice with difficulty: {difficulty}.
    Topics to focus on: {', '.join(topics) if topics else 'any CKAD topic'}.

    Refer to these manifests of the current Kubernetes cluster:
    {json.dumps(state.baseline_manifests, indent=2)}
    
    The challenge should:
    1. Be realistic and similar to actual CKAD exam questions
    2. Involve debugging issues in the Kubernetes cluster described by the manifests
    3. Have a clear objective and solution
    
    Return a response with:
    TITLE: [brief title]
    DESCRIPTION: [detailed description of the challenge]
    DIFFICULTY: [difficulty level]
    TOPICS: [comma-separated list of Kubernetes topics involved]
    HINTS: [3 progressive hints that help solve the challenge]
    """
    
    # Call LLM and parse response
    llm = ChatOpenAI(model="gpt-4o").with_structured_output(Challenge)
    response = llm.invoke(prompt)
    print("--- LLM challenge generated ---")
    print(response)
    
    return {
        "challenge": response
    }
