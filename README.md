# AI Text Intelligence 🚀

**Author:** Suresh Agrawal  

AI Text Intelligence is a full-stack, production-grade AI application that performs
**sentiment analysis (Positive / Neutral / Negative)** on user-provided text.

The system is built with a clean separation of concerns between:
- Frontend UI
- Backend API
- Machine Learning system
- Model Registry (MLflow)

This repository demonstrates **real-world AI product architecture**, not just a demo.

---

## ✨ Key Features

- Real-time sentiment prediction
- Confidence score based on ML probabilities
- Modern animated UI (Next.js + Tailwind)
- MLflow-based model versioning & registry
- Scalable Web → PWA → Mobile design

---

## 🧱 Architecture Overview

```
Frontend (Next.js)
        ↓
Backend API (FastAPI)
        ↓
MLflow Model Registry
        ↓
Trained ML Model
```

---

## 🛠 Technology Stack

| Layer | Technology |
|------|-----------|
| Frontend | Next.js (App Router), Tailwind CSS |
| Backend | FastAPI |
| ML | Scikit-learn |
| MLOps | MLflow |
| Deployment | Vercel, Render |

---

## 🚀 Recommended Deployment Order

1. MLflow Server
2. Backend API
3. Frontend Web App
4. PWA / Mobile App

---

## 📄 License

MIT License
