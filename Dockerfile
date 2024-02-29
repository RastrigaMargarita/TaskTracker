# Используем базовый образ Python
FROM python:3

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости в контейнер
COPY ./requirements .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements

# Копируем код приложения в контейнер
COPY . .
