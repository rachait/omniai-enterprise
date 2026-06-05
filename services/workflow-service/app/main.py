from fastapi import FastAPI

from .database import engine, Base
from .routes.workflow_routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="OmniAI Workflow Service"
)

app.include_router(router)

@app.get("/")
def root():
    return {
        "service": "Workflow Service Running"
    }
