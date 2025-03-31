#!/bin/bash

# Build and start the Docker container
cd "$(dirname "$0")/../docker"
docker build -t ckad-practice .
docker run -d --name ckad-practice-env \
    --privileged \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -p 6443:6443 \
    --network host \
    ckad-practice

echo "Environment is starting up..."
echo "Wait a few moments for the Kubernetes cluster to initialize"
echo "Use ./scripts/connect.sh to connect to the environment"
