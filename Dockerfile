FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    postgresql-client \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY .env .env

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=school_api.settings

ENTRYPOINT ["/entrypoint.sh"]

CMD ["uvicorn", "school_api.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
