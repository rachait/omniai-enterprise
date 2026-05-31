from fastapi import FastAPI

app = FastAPI(title="OmniAI Enterprise")

@app.get("/")
def root():
    return {
        "message": "OmniAI Enterprise API Gateway"
    }
