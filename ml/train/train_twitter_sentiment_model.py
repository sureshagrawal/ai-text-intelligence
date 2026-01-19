# =========================================================
# Twitter Sentiment Training Script (Phase-7)
# ---------------------------------------------------------
# - Dataset: Twitter_Sentiments.csv
# - Classes: positive / negative / neutral
# - MLflow-first, production ready
# =========================================================

import os
import pandas as pd
import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score


# ---------------------------------------------------------
# STEP 1: Paths & Constants
# ---------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "twitter",
    "Twitter_Sentiments.csv"
)

EXPERIMENT_NAME = "twitter-sentiment-analysis"
REGISTERED_MODEL_NAME = "TwitterSentimentModel"


# ---------------------------------------------------------
# STEP 2: Load Dataset
# ---------------------------------------------------------

def load_dataset(path: str) -> pd.DataFrame:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Dataset not found at: {path}")

    df = pd.read_csv(path)

    # Keep only required columns
    df = df[["text", "sentiment"]]

    # Drop nulls
    df = df.dropna()

    return df


# ---------------------------------------------------------
# STEP 3: Train Pipeline
# ---------------------------------------------------------

def build_pipeline() -> Pipeline:
    """
    Text preprocessing + classifier
    Preprocessing stays INSIDE pipeline
    """

    pipeline = Pipeline(
        steps=[
            (
                "vectorizer",
                TfidfVectorizer(
                    lowercase=True,
                    strip_accents="unicode",
                    max_features=5000,
                    ngram_range=(1, 2),
                ),
            ),
            (
                "classifier",
                LogisticRegression(
                    max_iter=1000,
                    multi_class="auto",
                    n_jobs=-1,
                ),
            ),
        ]
    )

    return pipeline


# ---------------------------------------------------------
# STEP 4: Training Logic
# ---------------------------------------------------------

def train():
    # Load data
    df = load_dataset(DATA_PATH)

    X = df["text"]
    y = df["sentiment"]

    # Train / validation split
    X_train, X_val, y_train, y_val = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    # Build pipeline
    model = build_pipeline()

    # MLflow setup
    mlflow.set_experiment(EXPERIMENT_NAME)

    with mlflow.start_run():
        # Train
        model.fit(X_train, y_train)

        # Predict
        y_pred = model.predict(X_val)

        # Metrics
        accuracy = accuracy_score(y_val, y_pred)
        f1_macro = f1_score(y_val, y_pred, average="macro")

        # Log metrics
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("f1_macro", f1_macro)

        # Log params
        mlflow.log_param("model_type", "LogisticRegression")
        mlflow.log_param("vectorizer", "TfidfVectorizer")
        mlflow.log_param("ngram_range", "1-2")
        mlflow.log_param("max_features", 5000)

        # Log model
        mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path="model",
            registered_model_name=REGISTERED_MODEL_NAME,
        )

        print("✅ Model trained & logged to MLflow")
        print(f"Accuracy  : {accuracy:.4f}")
        print(f"F1-macro  : {f1_macro:.4f}")


# ---------------------------------------------------------
# STEP 5: Entry Point
# ---------------------------------------------------------

if __name__ == "__main__":
    train()
