from app.core.config import settings


def get_predictor():

    if settings.ML_PREDICTOR_TYPE == "mlflow":
        from app.inference.mlflow_predictor import MLflowSentimentPredictor
        return MLflowSentimentPredictor()

    if settings.ML_PREDICTOR_TYPE == "http":
        from app.inference.http_predictor import HttpSentimentPredictor
        return HttpSentimentPredictor()

    if settings.ML_PREDICTOR_TYPE == "local":
        from app.inference.local_predictor import LocalSentimentPredictor
        return LocalSentimentPredictor()

    if settings.ML_PREDICTOR_TYPE == "hf":
        from app.inference.hf_predictor import HFSentimentPredictor
        return HFSentimentPredictor()

    raise RuntimeError(
        f"Unknown ML_PREDICTOR_TYPE: {settings.ML_PREDICTOR_TYPE}"
    )
