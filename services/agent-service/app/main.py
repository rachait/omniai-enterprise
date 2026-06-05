from fastapi import FastAPI

from .routes.agent_routes import router

app = FastAPI(
    title="OmniAI Agent Service"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "service": "Agent Service Running"
    }
