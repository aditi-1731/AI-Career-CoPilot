import google.generativeai as genai

from app.core.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)


class GeminiClient:
    def __init__(self):
        self.model = genai.GenerativeModel(settings.GEMINI_MODEL)

    def complete_json(self, system: str, user: str) -> str:
        """
        Calls Gemini with a forced JSON response format.
        Returns raw JSON text — no markdown fences, no preamble.
        """
        response = self.model.generate_content(
            [system, user],
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json",
                max_output_tokens=2000,
                temperature=0.4,
            ),
        )
        return response.text


def get_llm_client() -> GeminiClient:
    return GeminiClient()