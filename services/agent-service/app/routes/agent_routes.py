from fastapi import APIRouter
from dotenv import load_dotenv
from ..schemas import ChatRequest

import google.generativeai as genai
import os

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

router = APIRouter()


@router.post("/agents/chat")
def chat(request: ChatRequest):

    response = model.generate_content(
        request.message
    )

    return {
        "response": response.text
    }
