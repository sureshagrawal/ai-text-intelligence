FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install minimal dependencies for MLflow server
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy MLflow-related files (configs, etc.)
COPY . .

# Start MLflow server (Railway-compatible)
CMD ["sh", "-c", "mlflow server --host 0.0.0.0 --port $PORT --backend-store-uri $DATABASE_URL --default-artifact-root /mlflow/artifacts"]
