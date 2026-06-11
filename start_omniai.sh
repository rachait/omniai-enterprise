#!/bin/bash

docker compose -f infrastructure/docker/docker-compose.yml up -d

tmux new-session -d -s omniai

tmux send-keys -t omniai:0 "cd services/auth-service && source venv/bin/activate && uvicorn app.main:app --reload --port 8001" C-m

tmux split-window -h

tmux send-keys "cd services/workflow-service && source venv/bin/activate && uvicorn app.main:app --reload --port 8002" C-m

tmux split-window -v

tmux send-keys "cd services/execution-engine && source venv/bin/activate && uvicorn app.main:app --reload --port 8003" C-m

tmux split-window -v

tmux send-keys "cd services/agent-service && source venv/bin/activate && uvicorn app.main:app --reload --port 8004" C-m

tmux attach -t omniai
