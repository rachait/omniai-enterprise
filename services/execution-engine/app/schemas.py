from pydantic import BaseModel


class ExecutionResponse(BaseModel):
    id: int
    workflow_id: int
    status: str

    class Config:
        from_attributes = True
