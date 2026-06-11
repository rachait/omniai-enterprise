# OmniAI Enterprise 🚀

OmniAI Enterprise is an AI-powered workflow automation platform inspired by n8n, Flowise, Langflow, and Zapier AI.

The platform enables users to create, execute, and manage AI workflows using Large Language Models (LLMs), vector databases, message queues, and microservices.

---

# Architecture

```text
                   OmniAI Enterprise

                           Frontend
                               │
                               ▼
                         API Gateway
                               │
      ┌────────────────────────┼────────────────────────┐
      │                        │                        │
      ▼                        ▼                        ▼
 Auth Service          Workflow Service         Agent Service
    8001                    8002                   8004
                                │
                                ▼
                       Execution Engine
                             8003
                                │
      ┌──────────────┬──────────┴───────────┬─────────────┐
      ▼              ▼                      ▼             ▼
 PostgreSQL       Redis                RabbitMQ        Qdrant
```

---

# Tech Stack

## Backend

- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic

## AI & Data

- Google Gemini API
- Qdrant Vector Database
- Redis Cache

## Messaging

- RabbitMQ

## DevOps

- Docker
- Docker Compose
- GitHub

---

# Services

## Auth Service (Port 8001)

Features:

- User Registration
- User Login
- JWT Authentication

Endpoints:

```http
POST /auth/register
POST /auth/login
```

---

## Workflow Service (Port 8002)

Features:

- Create Workflow
- Get Workflow List
- Get Workflow By ID

Endpoints:

```http
POST /workflows
GET /workflows
GET /workflows/{workflow_id}
```

---

## Execution Engine (Port 8003)

Features:

- Execute Workflow
- Store Execution Records
- Connect to Agent Service

Endpoints:

```http
POST /executions/{workflow_id}
GET /executions
```

---

## Agent Service (Port 8004)

Features:

- Gemini AI Integration
- AI Chat API

Endpoints:

```http
POST /agents/chat
```

---

# Infrastructure

Services currently running:

- PostgreSQL
- Redis
- RabbitMQ
- Qdrant

Verify:

```bash
docker ps
```

---

# Current AI Workflow

```text
User
  │
  ▼
Execution Engine
  │
  ▼
Agent Service
  │
  ▼
Gemini AI
  │
  ▼
AI Response
```

---

# Running OmniAI

## Start Infrastructure

```bash
cd infrastructure/docker

docker compose up -d
```

---

## Start Auth Service

```bash
cd services/auth-service

source venv/bin/activate

uvicorn app.main:app --reload --port 8001
```

---

## Start Workflow Service

```bash
cd services/workflow-service

source venv/bin/activate

uvicorn app.main:app --reload --port 8002
```

---

## Start Execution Engine

```bash
cd services/execution-engine

source venv/bin/activate

uvicorn app.main:app --reload --port 8003
```

---

## Start Agent Service

```bash
cd services/agent-service

source venv/bin/activate

uvicorn app.main:app --reload --port 8004
```

---

# API Documentation

| Service | Swagger URL |
|----------|-------------|
| Auth Service | http://localhost:8001/docs |
| Workflow Service | http://localhost:8002/docs |
| Execution Engine | http://localhost:8003/docs |
| Agent Service | http://localhost:8004/docs |

---

# Implemented Features

- [x] Authentication Service
- [x] JWT Authentication
- [x] Workflow Service
- [x] Execution Engine
- [x] Agent Service
- [x] Gemini Integration
- [x] PostgreSQL Integration
- [x] Redis Setup
- [x] RabbitMQ Setup
- [x] Qdrant Setup
- [x] Docker Infrastructure

---

# Roadmap

## Workflow Engine

- [ ] Dynamic Workflow Execution
- [ ] Workflow Update API
- [ ] Workflow Delete API
- [ ] Execution Result Storage

## Frontend

- [ ] Next.js Dashboard
- [ ] Workflow Builder
- [ ] Execution History
- [ ] Authentication UI

## Advanced AI Features

- [ ] RAG Service
- [ ] Multi-Agent Workflows
- [ ] Tool Calling
- [ ] Memory Management

## DevOps

- [ ] CI/CD Pipeline
- [ ] Kubernetes Deployment
- [ ] Monitoring & Logging
- [ ] Production Deployment

---

# Project Status

### Infrastructure
100% Complete ✅

### Backend Core
75% Complete ✅

### AI Integration
80% Complete ✅

### Frontend
10% Complete ⏳

### Overall Progress
~65% Complete 🚀

---

# Author

**Rachait Talwar**

AI Engineer | Data Science | DevOps | Agentic AI
