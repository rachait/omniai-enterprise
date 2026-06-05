from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Execution

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

    return execution


@router.get("/executions")
def get_executions(
    db: Session = Depends(get_db)
):
    return db.query(Execution).all()
