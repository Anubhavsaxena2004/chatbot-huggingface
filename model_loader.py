# model_loader.py
import google.generativeai as genai
from config import API_KEY, MODEL_NAME

def load_model():
    """Loads the Gemini model"""
    genai.configure(api_key=API_KEY)
    return genai.GenerativeModel(MODEL_NAME)