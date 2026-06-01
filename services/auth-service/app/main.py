from fastapi import FastAPI

from .database import engine
from .models import Base
from .routes.auth_routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="OmniAI Auth Service"
)

app.include_router(
    router,
    prefix="/auth",
    tags=["Authentication"]
)


@app.get("/")
def root():
    return {
        "service": "OmniAI Auth Service Running"
    }
