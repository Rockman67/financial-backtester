FROM python:3.12-slim

# 1. Создаём рабочую папку
WORKDIR /app

# 2. Копируем requirements и устанавливаем пакеты
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Копируем только код web-приложения
COPY webui/ /app

# 4. Открываем порт и запускаем
EXPOSE 8000
CMD ["python", "app.py"]
