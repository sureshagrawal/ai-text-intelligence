# Backend – Sentiment Analysis API ⚙️

**Author:** Suresh Agrawal  

This backend service exposes REST APIs for sentiment analysis.
It loads a trained ML model from **MLflow Model Registry** and performs inference.

---

## 🚀 Tech Stack

- FastAPI
- MLflow (pyfunc)
- Python 3.11

---

## 📌 API Endpoints

### Health Check
```
GET /sentiment/health
```

Response:
```json
{ "status": "ok" }
```

---

### Analyze Sentiment
```
POST /sentiment/
```

Request:
```json
{
  "text": "I love this product"
}
```

Response:
```json
{
  "sentiment": "Positive",
  "confidence": 72,
  "source": "mlflow"
}
```

---

## ⚙️ Environment Variables

Create a `.env` file:

```
MLFLOW_TRACKING_URI=http://localhost:5000
MLFLOW_MODEL_URI=models:/TwitterSentimentModel/Production
```

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Swagger UI:
```
http://localhost:8000/docs
```

---

## 🧠 Notes

- Backend contains no ML training logic
- MLflow is the single source of truth
- Safe for future model upgrades
