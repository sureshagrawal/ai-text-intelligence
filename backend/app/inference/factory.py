from app.core.config import settings
from app.inference.mlflow_predictor import MLflowSentimentPredictor
from app.inference.http_predictor import HttpSentimentPredictor


def get_predictor():
    """
    Factory selector.

    Backend depends ONLY on this function.
    """

    if settings.ML_PREDICTOR_TYPE == "mlflow":
        return MLflowSentimentPredictor()

    if settings.ML_PREDICTOR_TYPE == "http":
        return HttpSentimentPredictor()

    raise RuntimeError(
        f"Unknown ML_PREDICTOR_TYPE: {settings.ML_PREDICTOR_TYPE}"
    )
