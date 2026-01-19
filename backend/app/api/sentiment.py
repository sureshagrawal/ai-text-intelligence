from fastapi import APIRouter
from app.schemas.sentiment_schema import (
    SentimentRequest,
    SentimentResponse
)
from app.services.sentiment_service import analyze_sentiment

router = APIRouter(prefix="/sentiment", tags=["Sentiment"])

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.post("/", response_model=SentimentResponse)
def sentiment(request: SentimentRequest):
    return analyze_sentiment(request.text)
