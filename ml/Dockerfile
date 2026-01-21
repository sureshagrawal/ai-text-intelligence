FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install only mlflow (no conflicts)
RUN pip install --no-cache-dir mlflow==2.9.2

# Railway provides PORT env var
EXPOSE 8080

# Start MLflow UI (local filesystem only)
CMD ["mlflow", "ui", "--host", "0.0.0.0", "--port", "8080"]
