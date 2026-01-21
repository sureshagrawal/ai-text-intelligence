FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy ML code
COPY . .

EXPOSE 5000

CMD mlflow server \
  --host 0.0.0.0 \
  --port $PORT \
  --backend-store-uri $DATABASE_URL \
  --default-artifact-root /mlflow/artifacts
