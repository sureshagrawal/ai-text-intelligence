"""
Application configuration (Environment-driven)

NOW USING:
- MLflow configuration via .env

Dummy defaults are kept BELOW (commented)
for reference / rollback.
"""

from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# -------------------------------------------------
# 🟢 ACTIVE — Load values from .env (Document-5)
# -------------------------------------------------
load_dotenv()   # enables reading .env file

class Settings(BaseSettings):
    MLFLOW_TRACKING_URI: str
    MLFLOW_MODEL_URI: str

settings = Settings()


# -------------------------------------------------
# 🔴 OLD — Dummy defaults [COMMENTED]
# -------------------------------------------------
"""
class Settings(BaseSettings):
    MLFLOW_TRACKING_URI: str = "http://localhost:5000"
    MLFLOW_MODEL_URI: str = "dummy"

settings = Settings()
"""
