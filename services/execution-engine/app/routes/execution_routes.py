from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Execution

import requests

router = APIRouter()


@router.post("/executions/{workflow_id}")
def execute_workflow(
    workflow_id: int,
    db: Session = Depends(get_db)
):
    execution = Execution(
        workflow_id=workflow_id,
        status="completed"
    )

    db.add(execution)
    db.commit()
    db.refresh(execution)

    agent_response = requests.post(
        "http://localhost:8004/agents/chat",
        json={
            "message": "Explain Agentic AI in simple words"
        }
    )

    ai_result = agent_response.json()

    return {
        "workflow_id": workflow_id,
        "status": "completed",
        "ai_response": ai_result
    }


@router.get("/executions")
def get_executions(
    db: Session = Depends(get_db)
):
    return db.query(Execution).all()
