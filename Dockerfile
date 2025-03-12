# Базовый образ
FROM python:3.13-slim

# Установка рабочей директории
WORKDIR /app

# Копирование зависимостей
COPY pyproject.toml .
RUN pip install --no-cache-dir -e .

# Копирование исходного кода
COPY src ./src
COPY migrations ./migrations
COPY alembic.ini .

# Команда для запуска приложения
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
