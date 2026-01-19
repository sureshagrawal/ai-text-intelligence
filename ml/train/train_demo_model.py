import mlflow
import mlflow.sklearn

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

texts = [
    "I love this product",
    "This is amazing",
    "Very happy with the service",
    "I hate this",
    "This is terrible",
    "Very bad experience",
    "It is okay",
    "Nothing special",
    "Average experience"
]

labels = [
    "Positive", "Positive", "Positive",
    "Negative", "Negative", "Negative",
    "Neutral", "Neutral", "Neutral"
]

mlflow.set_experiment("demo-sentiment-analysis")

with mlflow.start_run():

    pipeline = Pipeline([
        ("vectorizer", CountVectorizer()),
        ("model", MultinomialNB())
    ])

    pipeline.fit(texts, labels)

    mlflow.sklearn.log_model(
        sk_model=pipeline,
        artifact_path="model",
        registered_model_name="SentimentDemoModel"
    )

    print("✅ Pipeline model trained & logged to MLflow")
