#!/bin/bash

# Create and configure Kind cluster
echo "Creating Kind cluster..."
kind delete cluster --name ckad 2>/dev/null || true
kind create cluster --name ckad --config /home/practice/kind-config.yaml

# Wait for the API server to be ready
echo "Waiting for API server..."
until curl -k https://127.0.0.1:6443 >/dev/null 2>&1; do
    echo "Waiting for API server to be accessible..."
    sleep 2
done

# Set up kubeconfig
echo "Setting up kubeconfig..."
mkdir -p /root/.kube
kind export kubeconfig --name ckad

# Copy config to practice user
mkdir -p /home/practice/.kube
cp /root/.kube/config /home/practice/.kube/
chown -R practice:practice /home/practice/.kube

# Debug information
echo "Debug: Checking cluster access..."
kubectl cluster-info
echo "Debug: Checking nodes..."
kubectl get nodes

# Apply Kubernetes manifests
echo "Applying Kubernetes manifests..."
kubectl apply -f /home/practice/kubernetes/namespace.yaml
kubectl apply -f /home/practice/kubernetes/backend-deployment.yaml
kubectl apply -f /home/practice/kubernetes/frontend-deployment.yaml

echo "Waiting for deployments to be ready..."
kubectl wait --for=condition=Available deployment/backend -n practice-apps --timeout=60s || true
kubectl wait --for=condition=Available deployment/frontend -n practice-apps --timeout=60s || true

# Keep container running
tail -f /dev/null
