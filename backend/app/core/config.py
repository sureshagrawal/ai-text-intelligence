from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    """
    NOTE:
    -----
    These are FUTURE MLflow configs.
    Currently NOT USED because MLflow code is commented.

    They exist so that:
    - no refactor is needed later
    - only .env values change in deployment
    """
    MLFLOW_TRACKING_URI: str = "http://localhost:5000"
    MLFLOW_MODEL_URI: str = "dummy"

settings = Settings()
