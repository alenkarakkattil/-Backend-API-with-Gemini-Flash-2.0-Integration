from fastapi import FastAPI
from pydantic import BaseModel
from gemini_integration import get_gemini_response

app = FastAPI()

class PromptInput(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    return {"message": "Gemini FastAPI Backend is running!"}

@app.post("/generate/")
def generate_response(data: PromptInput):
    result = get_gemini_response(data.prompt)
    return {"response": result}