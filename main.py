from fastapi import FastAPI
from pydantic import BaseModel
from gemini_integration import get_gemini_response
import time

app = FastAPI()

class PromptInput(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    return {"message": "Gemini FastAPI Backend is running!"}

@app.post("/generate/")
def generate_response(data: PromptInput):
    print("Prompt:", data.prompt)
    start = time.time()
    
    response = get_gemini_response(data.prompt)
    
    end = time.time()
    latency = end - start

    print(f"Response Time: {latency:.2f}s")
    print("Gemini Response:", response)
    print("-" * 50)

    return {"response": response}
