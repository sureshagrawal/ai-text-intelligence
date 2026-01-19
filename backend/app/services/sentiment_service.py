import mlflow.pyfunc
from app.core.config import settings

_model = None

def _load_model():
    global _model
    if _model is None:
        _model = mlflow.pyfunc.load_model(
            settings.MLFLOW_MODEL_URI
        )
    return _model


def analyze_sentiment(text: str):
    if not text or not text.strip():
        raise ValueError("EMPTY_TEXT")

    model = _load_model()

    # Predict class
    pred = model.predict([text])[0]

    # Predict probabilities (for confidence)
    if hasattr(model, "_model_impl") and hasattr(model._model_impl, "predict_proba"):
        probs = model._model_impl.predict_proba([text])[0]
        confidence = round(float(max(probs)) * 100)
    else:
        confidence = 0

    return {
        "sentiment": pred.capitalize(),
        "confidence": confidence,
        "source": "mlflow",
    }
