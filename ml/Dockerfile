FROM python:3.11-slim

WORKDIR /app

# Install only MLflow server dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sh", "-c", "mlflow server --host 0.0.0.0 --port $PORT --backend-store-uri $DATABASE_URL"]
