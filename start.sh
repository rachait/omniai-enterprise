#!/bin/bash

cd infrastructure/docker
docker compose up -d

cd ~/projects/omniai-enterprise/services/auth-service
source venv/bin/activate
nohup uvicorn app.main:app --host 0.0.0.0 --port 8001 > auth.log 2>&1 &

cd ~/projects/omniai-enterprise/services/workflow-service
source venv/bin/activate
nohup uvicorn app.main:app --host 0.0.0.0 --port 8002 > workflow.log 2>&1 &

cd ~/projects/omniai-enterprise/services/execution-engine
source venv/bin/activate
nohup uvicorn app.main:app --host 0.0.0.0 --port 8003 > execution.log 2>&1 &

cd ~/projects/omniai-enterprise/services/agent-service
source venv/bin/activate
nohup uvicorn app.main:app --host 0.0.0.0 --port 8004 > agent.log 2>&1 &

echo "OmniAI Started"
