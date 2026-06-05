from pydantic import BaseModel
from typing import Dict, Any


class WorkflowCreate(BaseModel):
    name: str
    definition: Dict[str, Any]


class WorkflowResponse(BaseModel):
    id: int
    name: str
    definition: Dict[str, Any]

    class Config:
        from_attributes = True
