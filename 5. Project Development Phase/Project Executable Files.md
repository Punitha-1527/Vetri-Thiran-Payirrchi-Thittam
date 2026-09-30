# Project Executable Files

**Project:** EduGenie – Your Smart Budget & Recommendation Assistant  
**Team ID:** SWTID-2026-5933

| S.No | File / Command | Location | Purpose |
|---|---|---|---|
| 1 | requirements.txt | Project root | Lists Python dependencies |
| 2 | .env | Project root | Stores GEMINI_API_KEY, GEMINI_MODEL, SECRET_KEY, DATABASE_URL |
| 3 | app.py | Project root | Starts the Flask server |
| 4 | ml/train_model.py | ml | Trains and saves the category model |
| 5 | services/gemini_service.py | services | Calls the generative AI API |
| 6 | templates/index.html | templates | Main web page |

## Steps to Run

| Step | Command | Description |
|---|---|---|
| 1 | git clone <repository-url> | Download the project |
| 2 | pip install -r requirements.txt | Install dependencies |
| 3 | Create .env file | Add the keys listed above |
| 4 | python ml/train_model.py | Train the category model |
| 5 | python app.py | Start the server |
| 6 | Open http://localhost:5000 | Use EduGenie in the browser |
