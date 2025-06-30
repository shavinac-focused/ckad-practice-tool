import json
from typing import List, Dict
from chaos_agent.graph.state import Challenge, Mutation

def design_mutations(llm, challenge: Challenge, baseline_manifests: Dict[str, str]) -> List[Mutation]:
    """Design specific mutations to apply to the cluster based on the challenge"""
    # Use LLM to design specific mutations
    prompt = f"""
    Based on this challenge:
    {challenge.title}
    {challenge.description}
    
    And these baseline manifests:
    {json.dumps(baseline_manifests, indent=2)}
    
    Design specific mutations (changes) to apply to the Kubernetes cluster that will create the issues described in the challenge.
    Each mutation should be a kubectl command that can be executed to introduce a specific issue.
    
    Format your response as a list of mutations, each with:
    COMMAND: [kubectl command to execute]
    DESCRIPTION: [description of what this mutation does]
    RESOURCE_TYPE: [type of resource being modified]
    RESOURCE_NAME: [name of the resource]
    """
    
    # Call LLM and parse response
    # ...
