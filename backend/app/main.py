from fastapi import FastAPI
from app.api.sentiment import router as sentiment_router

app = FastAPI(title="Sentiment Analysis API")

app.include_router(sentiment_router)
