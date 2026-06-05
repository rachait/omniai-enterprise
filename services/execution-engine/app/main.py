from fastapi import FastAPI

from .database import engine, Base
from .routes.execution_routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="OmniAI Execution Engine"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "service": "Execution Engine Running"
    }
