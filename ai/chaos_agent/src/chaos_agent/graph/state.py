from typing import List, Dict, Optional
from pydantic import BaseModel, Field

class Challenge(BaseModel):
    """Represents a CKAD challenge scenario"""
    title: str
    description: str
    difficulty: str = "medium"  # easy, medium, hard
    topics: List[str] = []  # e.g., ["pods", "deployments", "services"]
    hints: List[str] = []

class Mutation(BaseModel):
    """Represents a change to the Kubernetes cluster"""
    kubectl_command: str
    description: str
    resource_type: str  # e.g., "deployment", "service", "pod"
    resource_name: str
    namespace: str = "practice-apps"
    applied: bool = False
    
class VerificationStep(BaseModel):
    """Represents a step to verify if the challenge is fixed"""
    command: str
    expected_output: str
    description: str

class GraphState(BaseModel):
    """State for the CKAD practice tool workflow"""
    # Challenge information
    challenge: Optional[Challenge] = None
    mutations: List[Mutation] = Field(default_factory=list)
    verification_steps: List[VerificationStep] = Field(default_factory=list)
    
    # Tracking information
    baseline_manifests: Dict[str, str] = Field(default_factory=dict)  # resource_key -> yaml
    attempt_count: int = 0
    is_challenge_active: bool = False
    is_challenge_solved: bool = False
    user_feedback: Optional[str] = None
    
    # Metrics
    start_time: Optional[float] = None
    solve_time: Optional[float] = None
