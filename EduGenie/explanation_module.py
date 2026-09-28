import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Global variables for local LaMini-Flan-T5 model
_tokenizer = None
_model = None
_model_attempted = False

def get_lamini_model():
    """Lazy-load the LaMini-Flan-T5 model if torch and transformers are available."""
    global _tokenizer, _model, _model_attempted
    if _model_attempted:
        return _tokenizer, _model
    _model_attempted = True
    try:
        from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
        import torch
        print("Loading local explanation model: MBZUAI/LaMini-Flan-T5-783M...")
        _tokenizer = AutoTokenizer.from_pretrained("MBZUAI/LaMini-Flan-T5-783M")
        _model = AutoModelForSeq2SeqLM.from_pretrained("MBZUAI/LaMini-Flan-T5-783M")
        print("LaMini-Flan-T5 model loaded successfully.")
    except Exception as e:
        print(f"Notice: Local LaMini model not initialized ({e}). Using Gemini for explanations.")
        _tokenizer = None
        _model = None
    return _tokenizer, _model

def explain_topic(topic: str) -> str:
    """
    Explain the concept in a simple and clear way for a school student.
    Uses MBZUAI/LaMini-Flan-T5-783M if loaded, with automatic Gemini fallback.
    """
    input_text = f"Explain the concept of '{topic}' in a simple and clear way for a school student."

    tokenizer, model = get_lamini_model()
    if tokenizer is not None and model is not None:
        try:
            inputs = tokenizer(input_text, return_tensors="pt")
            outputs = model.generate(
                **inputs,
                max_new_tokens=150,
                temperature=0.7,
                top_k=50,
                top_p=0.95,
                do_sample=True
            )
            explanation = tokenizer.decode(outputs[0], skip_special_tokens=True)
            return explanation
        except Exception as e:
            print(f"Local generation error: {e}. Falling back to Gemini.")

    # Fallback to Gemini
    try:
        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if not api_key:
            return "Please provide a valid Gemini API Key in the settings or .env file."
        genai.configure(api_key=api_key)
        
        try:
            gemini_model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")
            response = gemini_model.generate_content(input_text)
            return response.text.strip()
        except Exception:
            gemini_model = genai.GenerativeModel(model_name="gemini-1.5-flash")
            response = gemini_model.generate_content(input_text)
            return response.text.strip()
    except Exception as e:
        return f"Error in Explanation: {e}"
