import mlflow.pyfunc
from app.core.config import settings

_model = None


class MLflowSentimentPredictor:
    """
    MLflow-based predictor.

    ⚠️ FUTURE CHANGE:
    When ML inference moves to a separate HTTP service,
    this class will NOT be used by backend.
    No backend code will change.
    """

    def _load_model(self):
        global _model
        if _model is None:
            _model = mlflow.pyfunc.load_model(
                settings.MLFLOW_MODEL_URI
            )
        return _model

    def predict(self, text: str) -> dict:
        model = self._load_model()

        pred = model.predict([text])[0]

        # Best-effort confidence
        # ⚠️ FUTURE: BERT / RAG may compute this differently
        if hasattr(model, "_model_impl") and hasattr(model._model_impl, "predict_proba"):
            probs = model._model_impl.predict_proba([text])[0]
            confidence = round(float(max(probs)) * 100)
        else:
            confidence = 0

        return {
            "sentiment": pred.lower(),
            "confidence": confidence,
            "source": "inference",  # NOT mlflow (contract-safe)
        }
