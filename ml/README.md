# ML System – Twitter Sentiment Model 🧠

**Author:** Suresh Agrawal  

This module contains the complete **machine learning pipeline**
for training and registering a Twitter sentiment analysis model using MLflow.

---

## 📊 Dataset

- Twitter Sentiment Dataset
- Classes:
  - Positive
  - Neutral
  - Negative

Dataset location:
```
ml/data/twitter/Twitter_Sentiments.csv
```

---

## 🏋️ Model Training

### Install dependencies
```bash
pip install -r requirements.txt
```

### Train the model
```bash
python train/train_twitter_sentiment_model.py
```

Training will:
- Train the model
- Log metrics (accuracy, F1-score)
- Register the model in MLflow

---

## 📈 MLflow UI

```bash
mlflow ui
```

Open:
```
http://localhost:5000
```

---

## 🧪 Metrics Tracked

- Accuracy
- F1-macro

---

## 🔮 Future Enhancements

- Deep learning models
- Multilingual sentiment analysis
- Model monitoring & drift detection
