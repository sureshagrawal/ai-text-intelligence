from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    MLFLOW_TRACKING_URI: str
    MLFLOW_MODEL_URI: str

settings = Settings()
