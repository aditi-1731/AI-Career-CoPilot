import time

from google import genai
from google.genai import errors, types

from app.core.config import settings

_client = genai.Client(api_key=settings.GEMINI_API_KEY)


class LLMUnavailableError(Exception):
    """Raised when Gemini stays unavailable after retries and fallback."""


class GeminiClient:
    def __init__(self):
        self.models = [settings.GEMINI_MODEL]
        if settings.GEMINI_FALLBACK_MODEL:
            self.models.append(settings.GEMINI_FALLBACK_MODEL)

    def _call(self, model: str, system: str, user: str) -> str:
        response = _client.models.generate_content(
            model=model,
            contents=user,
            config=types.GenerateContentConfig(
                system_instruction=system,
                response_mime_type="application/json",
                max_output_tokens=8000,
                temperature=0.4,
            ),
        )
        if not response.text:
            raise ValueError("Model returned an empty response.")
        return response.text

    def complete_json(self, system: str, user: str, attempts_per_model: int = 2) -> str:
        """
        Forced-JSON completion. Retries 5xx errors, then tries the fallback model.
        """
        for model in self.models:
            for attempt in range(attempts_per_model):
                try:
                    return self._call(model, system, user)
                except errors.ServerError:
                    time.sleep(2 ** attempt)  # 1s, then 2s
        raise LLMUnavailableError("Gemini is temporarily unavailable.")


def get_llm_client() -> GeminiClient:
    return GeminiClient()