from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    # =================================
    # WHICH predictor to use
    # =================================
    ML_PREDICTOR_TYPE: str = "mlflow"

    # =================================
    # MLflow
    # =================================
    MLFLOW_TRACKING_URI: str | None = None
    MLFLOW_MODEL_URI: str | None = None

    # =================================
    # HTTP / HF inference
    # =================================
    ML_SERVICE_URL: str | None = None

    # ✅ ADD THIS LINE (VERY IMPORTANT)
    HF_TOKEN: str | None = None


settings = Settings()
