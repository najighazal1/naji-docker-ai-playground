from fastapi import FastAPI
from pydantic import BaseModel
from app.claude_client import analyze_code_with_claude

app = FastAPI()

class CodeRequest(BaseModel):
    code: str

@app.get("/")
def root():
    return {"message": "Docker AI Playground is running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/analyze")
def analyze_code(request: CodeRequest):
    result = analyze_code_with_claude(request.code)
    return {"analysis": result}
