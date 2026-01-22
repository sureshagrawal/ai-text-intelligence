import requests
from app.core.config import settings


class HFSentimentPredictor:
    """
    Production-safe HuggingFace Inference predictor
    ✔ handles cold start
    ✔ handles error JSON
    ✔ no crashes
    ✔ always returns valid schema
    """

    def predict(self, text: str) -> dict:
        headers = {
            "Authorization": f"Bearer {settings.HF_TOKEN}"
        }

        try:
            response = requests.post(
                settings.ML_SERVICE_URL,
                headers=headers,
                json={"inputs": text},
                timeout=30,
            )

            response.raise_for_status()
            data = response.json()

        except Exception as e:
            # network / timeout / HF down
            return {
                "sentiment": "unknown",
                "confidence": 0,
                "source": "huggingface-error"
            }

        # =========================
        # HF RESPONSE HANDLING
        # =========================

        # Case 1: HF returns error dict (model loading etc.)
        if isinstance(data, dict):
            return {
                "sentiment": "unknown",
                "confidence": 0,
                "source": "huggingface-loading"
            }

        # Case 2: normal success list
        result = data[0]

        label_map = {
            "LABEL_0": "negative",
            "LABEL_1": "neutral",
            "LABEL_2": "positive",
        }

        sentiment = label_map.get(result["label"], "unknown")

        # integer % like 97
        confidence = int(result["score"] * 100)

        return {
            "sentiment": sentiment,
            "confidence": confidence,
            "source": "huggingface"
        }
