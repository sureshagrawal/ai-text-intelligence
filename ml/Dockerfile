FROM python:3.11-slim

WORKDIR /app

# Install deps
COPY ml/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy ML code
COPY ml/ .

EXPOSE 5000

CMD mlflow server \
  --host 0.0.0.0 \
  --port 5000 \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root ./artifacts
