import re
import json
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def clean_json_block(text: str) -> str:
    """
    Remove Markdown ```json and ``` code fences and surrounding whitespace.
    """
    cleaned = re.sub(r"```(?:json)?\s*(.*?)\s*```", r"\1", text, flags=re.DOTALL).strip()
    # If starting/ending with triple backticks without closing:
    cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
    cleaned = re.sub(r"\s*```$", "", cleaned)
    return cleaned.strip()

def generate_quiz(text: str) -> list:
    """
    Generates 3 multiple-choice questions (MCQs) from a topic or passage.
    Returns a list of dicts with 'question', 'options' (4 items), and 'answer'.
    """
    try:
        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if not api_key:
            return [{"error": "Please provide a valid Gemini API Key in the settings or .env file."}]
        genai.configure(api_key=api_key)

        prompt = f"""You are a quiz generator.

From the following passage or topic, create 3 multiple-choice questions. Each question should include:
- A "question"
- A list of 4 "options"
- A correct "answer" that must exactly match one of the options.

Format your output as **valid JSON** ONLY, without extra explanation:
[
  {{
    "question": "What is ...?",
    "options": ["Option A", "Option B", "Option C", "Option D"],
    "answer": "Option A"
  }}
]

Passage:
{text}
"""
        try:
            model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")
            response = model.generate_content(prompt)
        except Exception as e_pro:
            print(f"Gemini 1.5 Pro unavailable ({e_pro}), trying gemini-1.5-flash...")
            model = genai.GenerativeModel(model_name="gemini-1.5-flash")
            response = model.generate_content(prompt)

        quiz_text = response.text.strip()
        cleaned_text = clean_json_block(quiz_text)

        # Attempt JSON decoding
        try:
            parsed = json.loads(cleaned_text)
            if isinstance(parsed, list):
                return parsed
            elif isinstance(parsed, dict) and "quiz" in parsed:
                return parsed["quiz"]
            return [parsed]
        except Exception:
            # Fallback: extract array using regex
            match = re.search(r"\[\s*\{.*\}\s*\]", cleaned_text, re.DOTALL)
            if match:
                return json.loads(match.group(0))
            raise ValueError(f"Could not parse JSON quiz from response: {cleaned_text}")

    except Exception as e:
        print(f"Error in quiz generation: {e}")
        return [{"error": f"Error in quiz generation: {e}"}]
