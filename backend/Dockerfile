FROM python:3.13.3-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:0.6.5 /uv /uvx /bin/

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Установка Python-пакетов
RUN pip install --no-cache-dir \
    --extra-index-url https://download.pytorch.org/whl/cpu \
    -r requirements.txt

ENV PYTHONPATH=/app/src

COPY . .
RUN apt-get -y update && apt-get -y install curl
RUN uv sync --frozen --no-cache

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
