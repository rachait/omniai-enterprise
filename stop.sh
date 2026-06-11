#!/bin/bash

pkill -f uvicorn

cd infrastructure/docker
docker compose down

echo "OmniAI Stopped"
