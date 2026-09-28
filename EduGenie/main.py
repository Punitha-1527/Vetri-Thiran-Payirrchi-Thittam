from fastapi import FastAPI, Request, Query
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import os
from pathlib import Path
from dotenv import load_dotenv, set_key

# Load environment variables
load_dotenv()

# Import module logic
from explanation_module import explain_topic
from qna import answer_question_with_gemini
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

app = FastAPI(
    title="EduGenie: Google Gemini Powered Learning Assistant",
    description="A lightweight AI-powered educational assistant for students and self-learners."
)

BASE_DIR = Path(__file__).resolve().parent

# Setup static files and templates
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# Root HTML Route
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    api_key_configured = bool(os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY"))
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"api_key_configured": api_key_configured}
    )

# Q&A - GET API using Gemini
@app.get("/qa")
async def answer_question(question: str = Query(..., description="The user's question")):
    answer = answer_question_with_gemini(question)
    return {"answer": answer}

# Explanation - POST API
@app.post("/explain")
async def explain_api(request: Request):
    data = await request.json()
    topic = data.get("topic")
    if not topic:
        return JSONResponse(content={"error": "Please provide a topic."}, status_code=400)
    explanation = explain_topic(topic)
    return {"topic": topic, "explanation": explanation}

# Summarization - POST API
@app.post("/summarize")
async def summarize_api(request: Request):
    data = await request.json()
    text = data.get("text")
    if not text:
        return JSONResponse(content={"error": "Please provide text to summarize."}, status_code=400)
    summary = summarize_text(text)
    return {"summary": summary}

# Quiz Generation - POST API
@app.post("/quiz")
async def quiz_api(request: Request):
    data = await request.json()
    text = data.get("text")
    if not text:
        return JSONResponse(content={"error": "Please provide text for quiz."}, status_code=400)
    quiz = generate_quiz(text)
    print("Generated quiz:", quiz) # DEBUG
    return JSONResponse(content={"quiz": quiz})

# Learning Recommendations - GET API
@app.get("/learn/recommendations")
async def learning_recommendation_api(topic: str = Query(..., description="The learning topic")):
    recommendation = get_learning_recommendations(topic)
    return {"topic": topic, "recommendation": recommendation}

# API Key configuration helper endpoints
class ApiKeyPayload(BaseModel):
    api_key: str

@app.get("/api/key-status")
async def get_key_status():
    has_key = bool(os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY"))
    return {"configured": has_key}

@app.post("/api/save-key")
async def save_api_key(payload: ApiKeyPayload):
    key = payload.api_key.strip()
    if not key:
        return JSONResponse(content={"error": "Key cannot be empty"}, status_code=400)
    os.environ["GEMINI_API_KEY"] = key
    env_file = BASE_DIR / ".env"
    try:
        set_key(str(env_file), "GEMINI_API_KEY", key)
    except Exception:
        with open(env_file, "a") as f:
            f.write(f"\nGEMINI_API_KEY={key}\n")
    return {"status": "success", "message": "API Key saved successfully!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
