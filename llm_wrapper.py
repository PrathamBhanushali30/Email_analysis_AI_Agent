import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class GeminiLLM:
    def __init__(self, model="gemini-pro"):
        self.model = genai.GenerativeModel(model)

    def call(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text