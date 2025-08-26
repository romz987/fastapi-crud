# Используем базовый образ Python
FROM python:3.12-slim

# Рабочая директория
WORKDIR /app

# Устанавливаем зависимости для apt и устанавливаем nano и neovim
# Чтобы если вдруг, то что-то можно было поправить прямо внутри контейнера
RUN apt-get update && apt-get install -y \
    nano \
    build-essential \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY . .

# Команда запуска
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
