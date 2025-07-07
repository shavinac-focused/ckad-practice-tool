import json
from typing import List
from pydantic import BaseModel
from chaos_agent.graph.state import Mutation, GraphState
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

class MutationList(BaseModel):
    mutations: List[Mutation]

def design_mutations(state: GraphState) -> GraphState:
    """Design specific mutations to apply to the cluster based on the challenge"""
    challenge = state.challenge
    baseline_manifests = state.baseline_manifests

    # Use LLM to design specific mutations
    prompt = f"""
    Based on this challenge:
    {challenge.title}
    {challenge.description}
    
    And these baseline manifests:
    {json.dumps(baseline_manifests, indent=2)}
    
    Design specific mutations (changes) to apply to the Kubernetes cluster that will create the issues described in the challenge.
    Each mutation should be a kubectl command that can be executed to introduce a specific issue.
    Keep the list of mutations small, only return 1-3 mutations for now.
    
    Format your response as a list of mutations, each with:
    COMMAND: [kubectl command to execute]
    DESCRIPTION: [description of what this mutation does]
    RESOURCE_TYPE: [type of resource being modified]
    RESOURCE_NAME: [name of the resource]
    """
    
    # Call LLM and parse response
    llm = ChatOpenAI(model="gpt-4o").with_structured_output(MutationList)
    response = llm.invoke(prompt)
    print("--- LLM mutations generated ---")
    print(response)
    
    return {
        "mutations": response.mutations
    }
