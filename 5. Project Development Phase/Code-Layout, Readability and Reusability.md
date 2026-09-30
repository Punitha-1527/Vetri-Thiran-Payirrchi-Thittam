# Code-Layout, Readability and Reusability

**Project:** EduGenie – Your Smart Budget & Recommendation Assistant  
**Team ID:** SWTID-2026-5933

## Project Folder Layout

```
edugenie/
├── app.py
├── requirements.txt
├── .env
├── config.py
├── routes/
│   ├── auth_routes.py
│   ├── expense_routes.py
│   ├── budget_routes.py
│   ├── forecast_routes.py
│   └── assistant_routes.py
├── services/
│   ├── categorizer.py
│   ├── forecaster.py
│   └── gemini_service.py
├── models/ (user.py, transaction.py, budget.py)
├── ml/ (train_model.py, category_model.pkl)
├── templates/ (index.html, dashboard.html)
└── static/ (style.css, script.js)
```

## Quality Criteria

| S.No | Criteria | How EduGenie Meets It | File / Module |
|---|---|---|---|
| 1 | Code Layout | Separate folders for routes, services, models, ML and UI | Project folders |
| 2 | Readability | Meaningful names, consistent style and comments on every function | All source files |
| 3 | Reusability | One generative AI service is reused for recommendations and chat; one ML service per task | services/ |
| 4 | Configuration Handling | Keys and database URL are read from environment variables | .env, config.py |
| 5 | Error Handling | Try-except blocks return clear JSON errors | routes/ |
| 6 | Security | Hashed passwords and token check on protected routes | auth_routes.py |
| 7 | Maintainability | Each feature is a separate route and service so it can change independently | routes/, services/ |
