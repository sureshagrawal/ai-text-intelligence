"""
This service will load ML model from MLflow registry.

Example (to be UNCOMMENTED later):

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
            "sentiment": prediction["label"],
            "confidence": prediction["confidence"],
            "source": "mlflow"
        }
"""

# 🔹 CURRENT (Document-3 ACTIVE LOGIC)

def analyze_sentiment(text: str):
    return {
        "sentiment": "Positive",
        "confidence": 0.95,
        "source": "dummy"
    }
