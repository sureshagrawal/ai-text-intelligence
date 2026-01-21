from app.inference.factory import get_predictor


def analyze_sentiment(text: str):
    if not text or not text.strip():
        raise ValueError("EMPTY_TEXT")

    predictor = get_predictor()

    # Backend has NO idea:
    # - where model is
    # - how prediction happens
    # - which framework is used
    return predictor.predict(text)
