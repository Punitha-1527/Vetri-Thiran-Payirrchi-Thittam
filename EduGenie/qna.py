import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def answer_question_with_gemini(question: str) -> str:
    """
    Answers general knowledge and academic questions using Google Gemini.
    """
    try:
        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if not api_key:
            return "Please provide a valid Gemini API Key in the settings or .env file."
        genai.configure(api_key=api_key)

        try:
            model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")
            response = model.generate_content(question)
            return response.text.strip()
        except Exception as e_pro:
            print(f"Gemini 1.5 Pro unavailable ({e_pro}), trying gemini-1.5-flash...")
            model = genai.GenerativeModel(model_name="gemini-1.5-flash")
            response = model.generate_content(question)
            return response.text.strip()
    except Exception as e:
        return f"Error in QnA: {e}"
