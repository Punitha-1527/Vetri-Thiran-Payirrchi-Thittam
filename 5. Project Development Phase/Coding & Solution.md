# Coding & Solution

**Project:** EduGenie – Your Smart Budget & Recommendation Assistant  
**Team ID:** SWTID-2026-5933

## Technology Used

| S.No | Layer | Technology |
|---|---|---|
| 1 | Frontend | HTML, CSS, JavaScript, Chart.js |
| 2 | Backend | Python, Flask |
| 3 | Machine Learning | scikit-learn, pandas |
| 4 | Generative AI | Google Gemini API |
| 5 | Database | SQLite / MongoDB |
| 6 | Security | JWT, password hashing, dotenv |

## Module-wise Implementation

| S.No | Module | API Endpoint | Description | Developed By |
|---|---|---|---|---|
| 1 | Authentication | POST /api/register, POST /api/login | Register and log in users | Madhan |
| 2 | Expense Tracking | POST /api/expenses, GET /api/expenses | Add and list transactions | Madhan |
| 3 | Auto Categorisation | POST /api/categorize | Predicts category from the expense description | Madhan |
| 4 | Budget Planner | POST /api/budget, GET /api/budget/alerts | Sets limits and returns alerts | Haridha |
| 5 | Spending Forecast | GET /api/forecast | Predicts next month's spending | Madhan, Punitha K |
| 6 | AI Recommendations | GET /api/recommendations | Personalised saving tips from spending summary | Punitha K |
| 7 | Budget Chat | POST /api/chat | Answers money questions using user data | Punitha K |
| 8 | User Interface | Frontend pages | Dashboard, forms and charts | Haridha |

## Core Services (Sample)

```python
# services/categorizer.py
import joblib
model = joblib.load("ml/category_model.pkl")

def predict_category(description: str) -> str:
    return model.predict([description])[0]
```

```python
# services/gemini_service.py
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(os.getenv("GEMINI_MODEL"))

def get_saving_tips(summary: str) -> str:
    prompt = f"Give 3 practical saving tips based on this monthly spending: {summary}"
    return model.generate_content(prompt).text
```
