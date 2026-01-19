from fastapi import APIRouter, HTTPException
from app.schemas.sentiment_schema import (
    SentimentRequest,
    SentimentResponse,
)
from app.services.sentiment_service import analyze_sentiment

router = APIRouter(prefix="/sentiment", tags=["Sentiment"])


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/", response_model=SentimentResponse)
def sentiment(request: SentimentRequest):
    try:
        return analyze_sentiment(request.text)
    except ValueError as e:
        if str(e) == "EMPTY_TEXT":
            raise HTTPException(status_code=400, detail="Text cannot be empty")
        raise HTTPException(status_code=500, detail="Inference failed")
