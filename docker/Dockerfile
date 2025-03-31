FROM ubuntu:22.04

# Install required packages
RUN apt-get update && apt-get install -y \
    curl \
    sudo \
    git \
    vim \
    docker.io \
    && rm -rf /var/lib/apt/lists/*

# Install kubectl
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" \
    && chmod +x kubectl \
    && mv kubectl /usr/local/bin/

# Install kind
RUN curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64 \
    && chmod +x ./kind \
    && mv ./kind /usr/local/bin/

# Create practice user
RUN useradd -m -s /bin/bash practice \
    && adduser practice sudo \
    && echo "practice ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Copy Kind config
COPY kind-config.yaml /home/practice/kind-config.yaml
RUN chown practice:practice /home/practice/kind-config.yaml

# Copy Kubernetes manifests
RUN mkdir -p /home/practice/kubernetes
COPY kubernetes /home/practice/kubernetes
RUN chown -R practice:practice /home/practice/kubernetes

# Expose ports
EXPOSE 6443

# Start cluster
COPY start.sh /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]
