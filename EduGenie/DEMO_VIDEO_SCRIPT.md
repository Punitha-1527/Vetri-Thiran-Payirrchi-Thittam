# 🎬 EduGenie: Demo Video Recording Script

**Project Title:** EduGenie: Google Gemini Powered Learning Assistant  
**Target Duration:** ~2:30 to 3:00 minutes  
**Format:** Screen Recording + Voiceover Presentation  

---

## ⏱️ Video Timeline Overview

| Section | Content | Estimated Time |
| :--- | :--- | :--- |
| **Part 0** | Intro & Project Overview | `0:00 - 0:15` (15s) |
| **Part 1** | Code Files Walkthrough (10s per key component) | `0:15 - 1:15` (60s) |
| **Part 2** | Live Web Dashboard Demonstration (Feature by Feature) | `1:15 - 2:45` (90s / 1.5 min) |
| **Part 3** | Conclusion & Wrap-up | `2:45 - 3:00` (15s) |

---

## 🎙️ SECTION 0: Introduction (0:00 - 0:15)

- **On Screen:** Title slide or VS Code showing the project directory `EduGenie`.
- **Action:** Smile and introduce yourself and the project.
- **Voiceover:**
  > *"Hello everyone! Welcome to the demo of **EduGenie**, an AI-powered personalized learning assistant built using **FastAPI**, **Google Gemini**, and a responsive modern web dashboard. In this video, I will walk you through our backend code architecture and demonstrate all interactive features of our live application."*

---

## 💻 SECTION 1: Code Architecture Walkthrough (0:15 - 1:15)
*(~10 seconds per file / component)*

### 1. `main.py` [0:15 - 0:25] (10s)
- **On Screen:** Open [`main.py`](file:///c:/Users/Nandhini/OneDrive/Desktop/NM%20project/Edu-Genie/main.py). Highlight lines defining routes (`/qa`, `/explain`, `/summarize`, `/quiz`, `/learn/recommendations`).
- **Voiceover:**
  > *"Starting with `main.py`—this is our FastAPI server. It mounts our static CSS, serves the Jinja2 HTML template, and sets up 5 clean RESTful endpoints: `/qa`, `/explain`, `/summarize`, `/quiz`, and `/learn/recommendations`, routing user requests directly to their respective logic modules."*

### 2. `qna.py` [0:25 - 0:35] (10s)
- **On Screen:** Open [`qna.py`](file:///c:/Users/Nandhini/OneDrive/Desktop/NM%20project/Edu-Genie/qna.py). Highlight `answer_question_with_gemini`.
- **Voiceover:**
  > *"Next is `qna.py`. It integrates Google Gemini to handle academic and general knowledge questions. It extracts the API key, generates context-aware answers, and has built-in fallback handling between Gemini 1.5 Pro and Gemini 1.5 Flash for high reliability."*

### 3. `explanation_module.py` [0:35 - 0:45] (10s)
- **On Screen:** Open [`explanation_module.py`](file:///c:/Users/Nandhini/OneDrive/Desktop/NM%20project/Edu-Genie/explanation_module.py). Highlight `explain_topic` and prompt structure.
- **Voiceover:**
  > *"Here is `explanation_module.py`. Designed to simplify complex concepts for school students, it supports the local `LaMini-Flan-T5` model for CPU-efficient inference, with automatic cloud Gemini fallback to guarantee instant explanations without delay."*

### 4. `quiz_module.py` [0:45 - 0:55] (10s)
- **On Screen:** Open [`quiz_module.py`](file:///c:/Users/Nandhini/OneDrive/Desktop/NM%20project/Edu-Genie/quiz_module.py). Highlight `clean_json_block` and JSON parsing.
- **Voiceover:**
  > *"Moving to `quiz_module.py`—it prompts Gemini to produce exactly 3 multiple-choice questions with 4 options and the correct answer. It features a custom `clean_json_block` function that strips Markdown code fences and parses the result into structured JSON for the frontend."*

### 5. `summary_module.py` & `learning_path.py` [0:55 - 1:05] (10s)
- **On Screen:** Split screen or quick switch between [`summary_module.py`](file:///c:/Users/Nandhini/OneDrive/Desktop/NM%20project/Edu-Genie/summary_module.py) and [`learning_path.py`](file:///c:/Users/Nandhini/OneDrive/Desktop/NM%20project/Edu-Genie/learning_path.py).
- **Voiceover:**
  > *"`summary_module.py` condenses long educational passages into digestible key points. Alongside it, `learning_path.py` creates customized roadmaps covering Beginner, Intermediate, and Advanced milestones with recommended books, tutorials, and timelines."*

### 6. `templates/index.html` & `static/style.css` [1:05 - 1:15] (10s)
- **On Screen:** Show [`templates/index.html`](file:///c:/Users/Nandhini/OneDrive/Desktop/NM%20project/Edu-Genie/templates/index.html) and [`static/style.css`](file:///c:/Users/Nandhini/OneDrive/Desktop/NM%20project/Edu-Genie/static/style.css).
- **Voiceover:**
  > *"Finally, our frontend in `index.html` and `style.css` provides a modern card-based interface with asynchronous Fetch API calls, dynamic markdown rendering, and interactive quiz grading."*

---

## 🌐 SECTION 2: Live Web Dashboard Demo (1:15 - 2:45)
*(1.5 minutes hands-on demonstration)*

- **On Screen:** Switch to browser showing **`http://127.0.0.1:8000`**.

### 1. Dashboard Overview & API Connection [1:15 - 1:25] (10s)
- **Action:** Scroll smoothly over the homepage. Point cursor to the top API Status bar.
- **Voiceover:**
  > *"Now let's see EduGenie in action! Here is our web dashboard running on port 8000. At the top, we have an API status bar allowing students or evaluators to connect their Gemini API key instantly without touching the command line."*

### 2. Feature 1: Ask EduGenie a Question [1:25 - 1:40] (15s)
- **Action:**
  - Type in: `"Which is the largest ocean?"`
  - Click **Get Answer**.
  - Show the loading spinner and the result card appearing below.
- **Voiceover:**
  > *"First, let's ask a question: 'Which is the largest ocean?'. I click 'Get Answer'. In real-time, EduGenie queries Gemini and returns a clear, concise answer: 'The Pacific Ocean is the largest ocean on Earth.'"*

### 3. Feature 2: Need an Explanation? [1:40 - 1:55] (15s)
- **Action:**
  - Scroll to the explanation section.
  - Type: `"Photosynthesis"` (or `"Quantum computing"`).
  - Click **Explain**.
  - Highlight the simplified explanation for students.
- **Voiceover:**
  > *"Second, for students struggling with difficult topics, our explanation module breaks concepts down into plain language. Entering 'Photosynthesis' and clicking 'Explain' gives a student-friendly explanation focusing on sunlight, chlorophyll, and glucose."*

### 4. Feature 3: Summarize a Paragraph [1:55 - 2:10] (15s)
- **Action:**
  - Paste a short paragraph (e.g., about the Industrial Revolution).
  - Click **Summarize**.
  - Show the condensed bullet-points/summary.
- **Voiceover:**
  > *"Third, the summarization tool. Students can paste long textbook excerpts, click 'Summarize', and receive an easy-to-read summary retaining the key takeaways for quick exam revision."*

### 5. Feature 4: Interactive Quiz Generator [2:10 - 2:30] (20s)
- **Action:**
  - Enter topic: `"The Pythagoras Theorem"`.
  - Click **Generate Quiz**.
  - Show 3 questions rendered with radio buttons.
  - Select the correct option for Q1 &rarr; Click **Check Answer** &rarr; Show `✅ Correct!`.
  - Intentionally select a wrong option for Q2 &rarr; Click **Check Answer** &rarr; Show `❌ Incorrect. Correct answer: a² + b² = c²`.
- **Voiceover:**
  > *"Fourth is one of EduGenie's best features: the Quiz Generator. I'll enter 'The Pythagoras Theorem' and click 'Generate Quiz'. It immediately creates 3 multiple choice questions with 4 options each! Notice it's fully interactive—if I select an answer and click 'Check Answer', it immediately validates with green for correct, or red showing the right formula if wrong!"*

### 6. Feature 5: Personalized Learning Roadmap [2:30 - 2:45] (15s)
- **Action:**
  - Enter: `"SQL"` in the recommendations field.
  - Click **Get Recommendations**.
  - Scroll through the rendered markdown roadmap showing Beginner, Intermediate, Advanced levels, timelines, and resources.
- **Voiceover:**
  > *"Finally, the Learning Recommendations module. When an aspiring developer asks for 'SQL', EduGenie produces an adaptive curriculum divided into Beginner, Intermediate, and Advanced stages, complete with time estimates and trusted tutorials."*

---

## 🎯 SECTION 3: Conclusion & Wrap-up (2:45 - 3:00)

- **On Screen:** Scroll back to top or show EduGenie header.
- **Action:** Concluding remarks.
- **Voiceover:**
  > *"In summary, EduGenie bridges the gap between state-of-the-art Generative AI and accessible learning by combining FastAPI with Google Gemini in an intuitive, responsive interface. Thank you for watching!"*

---

## 💡 Quick Tips for Recording
1. **Screen Resolution:** Record at `1920x1080` (1080p) with 100% or 110% browser zoom for crisp text.
2. **Terminal / Editor Layout:** Use a clean dark theme in VS Code (like Dark+ or One Dark Pro) with font size ~15px.
3. **Pre-test:** Make sure the server is already running (`uvicorn main:app`) so there is zero waiting time during your demo.
4. **Sample Inputs to keep ready in clipboard:**
   - Question: `Which is the largest ocean?`
   - Explanation: `Photosynthesis`
   - Summary: `The Industrial Revolution was a period of global transition of the human economy towards more widespread and efficient manufacturing processes that succeeded the Agricultural Revolution.`
   - Quiz: `The Pythagoras Theorem`
   - Learning Path: `SQL`
