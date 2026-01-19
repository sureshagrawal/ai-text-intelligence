"""
Sentiment Service Layer

NOW USING: MLflow registered model (Demo)

Dummy logic is kept BELOW (commented)
for reference / rollback if needed.
"""

# =================================================
# 🟢 ACTIVE — MLflow-based inference (Document-5)
# =================================================
import mlflow.pyfunc
from app.core.config import settings

_model = None

def load_model():
    global _model
    if _model is None:
        _model = mlflow.pyfunc.load_model(
            settings.MLFLOW_MODEL_URI
        )
    return _model


def analyze_sentiment(text: str):
    model = load_model()
    prediction = model.predict([text])[0]

    return {
        "sentiment": prediction,
        "confidence": 0.90,   # demo confidence
        "source": "mlflow"
    }

# =================================================
# 🔴 OLD — Dummy logic [COMMENTED]
# =================================================
"""
def analyze_sentiment(text: str):
    return {
        "sentiment": "Positive",
        "confidence": 0.95,
        "source": "dummy"
    }
"""
