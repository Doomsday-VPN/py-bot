# Базовый образ
FROM python:3.11-slim

WORKDIR /app
COPY /app .

RUN pip install --no-cache-dir -r requirements.txt

ARG BOT_TOKEN
ENV BOT_TOKEN=${BOT_TOKEN}

CMD ["python", "main.py"]