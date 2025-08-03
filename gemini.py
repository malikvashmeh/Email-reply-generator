
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


class GeminiReplyGenerator:
    def __init__(self):
        self.model = genai.GenerativeModel("models/gemini-1.0-pro")

    def generate_reply(self, email: str, role: str, tone: str) -> str:
        prompt = f"""
You are an assistant helping a user respond to an email.
The user is a {role} and wants the response to be in a {tone} tone.
Here is the received email:
{email}

Write a clear, professional reply that matches the tone and role. Keep it appropriate for business communication.
"""
        response = self.model.generate_content(prompt)
        return response.text.strip()

