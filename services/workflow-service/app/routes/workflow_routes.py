from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Workflow
from ..schemas import WorkflowCreate

router = APIRouter()


@router.post("/workflows")
def create_workflow(
    workflow: WorkflowCreate,
    db: Session = Depends(get_db)
):
    new_workflow = Workflow(
        name=workflow.name,
        definition=workflow.definition
    )

    db.add(new_workflow)
    db.commit()
    db.refresh(new_workflow)

    return new_workflow


@router.get("/workflows")
def get_workflows(
    db: Session = Depends(get_db)
):
    return db.query(Workflow).all()
