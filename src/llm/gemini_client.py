import google.generativeai as genai
from core.config import Config

class GeminiClient:
    def __init__(self):
        genai.configure(api_key=Config.GEMINI_API_KEY)
        self.model = genai.GenerativeModel("gemini-3-flash-preview")

    def generate(self, prompt: str, temperature: float = 0):
        response = self.model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                temperature=temperature
            )
        )
        return response.text.strip()