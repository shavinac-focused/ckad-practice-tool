import subprocess
import json
from typing import Dict

def kubectl_exec(command: str, namespace: str = "practice-apps") -> str:
    """Execute kubectl command inside the Docker container"""
    # Use subprocess to run docker exec command that runs kubectl inside the container
    if command.startswith("kubectl "):
        full_command = f"docker exec ckad-practice-env {command}"
    else:
        full_command = f"docker exec ckad-practice-env kubectl -n {namespace} {command}"
    # print(f"Executing command: {full_command}") # DEBUG
    result = subprocess.run(full_command, shell=True, capture_output=True, text=True)
    return result.stdout

def patch_yaml(resource_type: str, resource_name: str, patch: Dict, namespace: str = "practice-apps") -> str:
    """Apply a patch to a Kubernetes resource"""
    patch_json = json.dumps(patch)
    return kubectl_exec(f"patch {resource_type} {resource_name} --patch '{patch_json}'", namespace)
