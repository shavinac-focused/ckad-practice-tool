# CKAD Practice Tool

A local practice environment for the Certified Kubernetes Application Developer (CKAD) exam.

## Features

- Local Kubernetes cluster running in Docker
- Interactive practice questions
- Web interface for questions and answers

## Prerequisites

- Docker
- Node.js (v18 or later)
- Git

## Quick Start

1. Clone this repository
2. Start the practice environment:
   ```bash
   ./scripts/start-env.sh
   ```
3. Start the webapp:
   ```bash
   cd webapp
   npm install
   npm start
   ```
4. Visit http://localhost:3000 in your browser
5. To access the Kubernetes environment:

   ```bash
   ./scripts/connect.sh

   # run kubectl commands
   ```

6. To try the "chaos agent":
   ```bash
   ./scripts/start-env.sh # start the practice environment, if needed
   docker exec ckad-practice-env kubectl get all -n practice-apps # check that the environment is running

   cd ai/chaos_agent
   cp .env.example .env # make sure to provide API keys
   uv run -m chaos_agent.main
   ```

## Project Structure

```
.
├── docker/             # Docker and Kubernetes environment
├── webapp/            # Web application (HTML/JS/Node.js)
└── scripts/           # Helper scripts for environment management
```

## Development

This project is designed to be simple and extensible. The web application uses plain HTML/CSS/JavaScript with a Node.js backend, and the Kubernetes environment runs in a Docker container using Kind.

## License

MIT
