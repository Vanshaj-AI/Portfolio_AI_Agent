from google import genai
from langsmith import wrappers
from core.config import Config


class GeminiClient:
    def __init__(self):
        gemini_client = genai.Client(
            api_key=Config.GEMINI_API_KEY)

        # Wrap with LangSmith tracing
        self.client = wrappers.wrap_gemini(
            gemini_client,
            tracing_extra={
                "tags": ["gemini"],
                "metadata": {
                    "service": "gemini-client"
                }})

        self.model = "gemini-3-flash-preview"

    def generate(
        self,
        prompt: str,
        temperature: float = 0
    ):

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config={
                "temperature": temperature
            }
        )

        return response.text.strip()