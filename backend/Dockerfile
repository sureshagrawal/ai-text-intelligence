# =========================
# Base image
# =========================
FROM python:3.11-slim

# =========================
# System settings
# =========================
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# =========================
# Workdir
# =========================
WORKDIR /app

# =========================
# Install dependencies
# =========================
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# =========================
# Copy project
# =========================
COPY . .

# =========================
# Render provides PORT env
# =========================
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
