# EduGenie: Google Gemini Powered Learning Assistant

EduGenie is a lightweight AI-powered educational assistant that simplifies learning through generative AI. Designed for students of all academic levels, EduGenie enables users to:
- Ask questions and receive smart, concise answers (`/qa`)
- Understand complex concepts through simplified explanations (`/explain`)
- Generate interactive quizzes from topics or text (`/quiz`)
- Summarize large educational passages (`/summarize`)
- Receive personalized learning recommendations and roadmaps (`/learn/recommendations`)

Built with **FastAPI** for the backend and an intuitive **HTML + CSS** frontend.

---

## 📁 Project Architecture

```
EduGenie/
├── main.py                     # FastAPI application & REST API routing
├── explanation_module.py       # Concept explanation logic (LaMini-Flan-T5 / Gemini)
├── qna.py                      # Question answering powered by Gemini
├── quiz_module.py              # 3-question MCQ quiz generation with JSON parsing
├── summary_module.py           # Educational passage summarization
├── learning_path.py            # Structured learning roadmap & resource generator
├── templates/
│   └── index.html              # HTML frontend with interactive components
├── static/
│   └── style.css               # Clean, responsive CSS styling
├── requirements.txt            # Python dependencies
├── .env                        # Environment file for Gemini API Key
└── run.bat                     # 1-click startup batch script
```

---

## 🚀 Quick Setup & Run

### 1. Configure Your Gemini API Key
Obtain a free Gemini API key from [Google AI Studio](https://aistudio.google.com/).

You can set it in any of the following ways:
- **Option A:** Enter it directly into the `.env` file:
  ```env
  GEMINI_API_KEY=your_actual_api_key_here
  ```
- **Option B:** Enter it directly in the web UI at the top input bar and click **Save Key**.

### 2. Start the Server
Run the batch file:
```cmd
run.bat
```
Or run directly via PowerShell/Terminal:
```powershell
& "..\Edu-Genie\.venv\Scripts\python.exe" -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### 3. Open in Browser
Navigate to:
```
http://127.0.0.1:8000
```

---

## 🎯 Verification Scenarios (from Project Specification)

- **Scenario 1 (Q&A):** Ask *"Which is the largest ocean?"* &rarr; Click **Get Answer**.
- **Scenario 2 (Explanation):** Enter *"Photosynthesis"* or *"Quantum computing"* &rarr; Click **Explain**.
- **Scenario 3 (Summary):** Paste long text &rarr; Click **Summarize**.
- **Scenario 4 (Quiz):** Enter *"The Pythagoras Theorem"* or *"Solar System"* &rarr; Click **Generate Quiz** &rarr; Select radio options &rarr; Click **Check Answer** for real-time feedback.
- **Scenario 5 (Learning Path):** Enter *"SQL"* or *"Linear Regression"* &rarr; Click **Get Recommendations**.
