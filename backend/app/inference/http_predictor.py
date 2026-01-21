import requests
from app.core.config import settings


class HttpSentimentPredictor:
    """
    HTTP-based predictor.

    ⚠️ FUTURE CHANGE:
    This will call a standalone ML inference service.
    Backend code will remain unchanged.
    """

    def predict(self, text: str) -> dict:
        response = requests.post(
            settings.ML_SERVICE_URL,
            json={"text": text},
            timeout=5,
        )

        response.raise_for_status()
        return response.json()
