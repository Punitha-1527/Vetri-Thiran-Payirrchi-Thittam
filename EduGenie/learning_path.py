import os
import google.generativeai as genai
import traceback
from dotenv import load_dotenv

load_dotenv()

def get_learning_recommendations(topic: str) -> str:
    """
    Generates a personalized, structured learning path for any given topic
    spanning beginner to advanced levels with timelines and resources.
    """
    prompt = f"""You are an AI tutor. The student wants to learn about: {topic}.
Suggest a structured and adaptive learning path including key topics, order of learning, and resources (interactive tutorials, documentation, books, videos).
Include beginner, intermediate, and advanced levels with estimated timelines and adaptive learning tips.
"""
    try:
        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if not api_key:
            return "Please provide a valid Gemini API Key in the settings or .env file."
        genai.configure(api_key=api_key)

        try:
            model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")
            response = model.generate_content(prompt)
        except Exception as e_pro:
            print(f"Gemini 1.5 Pro unavailable ({e_pro}), trying gemini-1.5-flash...")
            model = genai.GenerativeModel(model_name="gemini-1.5-flash")
            response = model.generate_content(prompt)

        print("Gemini raw response:", response)

        if hasattr(response, "text"):
            return response.text
        elif hasattr(response, "parts") and response.parts:
            return response.parts[0].text
        else:
            return "Could not extract content from Gemini response."
    except Exception as e:
        traceback.print_exc()
        return f"Error occurred: {str(e)}"
