FROM python:3.9-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.9-slim

WORKDIR /app
COPY --from=builder /app /app
COPY app.py .

# Environment variables
ENV FLASK_APP=app.py
ENV DATABASE_URL=sqlite:///create_db.db

# Expose the port
EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
