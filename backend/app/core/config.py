from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    # Controls WHICH inference system backend uses
    # Today: mlflow
    # Future: http
    ML_PREDICTOR_TYPE: str = "mlflow"

    # MLflow config (used only for mlflow predictor)
    MLFLOW_TRACKING_URI: str | None = None
    MLFLOW_MODEL_URI: str | None = None

    # HTTP ML service config (used only for http predictor)
    ML_SERVICE_URL: str | None = None


settings = Settings()
