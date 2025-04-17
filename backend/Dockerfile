FROM python:3.11-slim

# Установка ffmpeg и очистка кэша в ОДИН RUN-слой (для уменьшения размера образа)
RUN apt-get update && apt-get install -y ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Сначала копируем только зависимости для кэширования
COPY requirements.txt .

# Установка Python-пакетов (добавлен torch для CPU)
RUN pip install --no-cache-dir -r requirements.txt \
    torch torchaudio --index-url https://download.pytorch.org/whl/cpu

# Копируем остальные файлы
COPY . .

# Проверка зависимостей
RUN ffmpeg -version && \
    python -c "import whisper; print(f'Whisper version: {whisper.__version__}')"

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]