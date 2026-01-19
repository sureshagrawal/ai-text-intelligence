from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.sentiment import router as sentiment_router

app = FastAPI(title="Sentiment Analysis API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",     # local frontend
        # "https://your-frontend.vercel.app"  # add later in prod 
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sentiment_router)
