# ---------- base ----------
FROM python:3.12-slim

# ---------- workdir ----------
WORKDIR /app

# ---------- dependencies ----------
# 1. копируем requirements.txt из корня репозитория
COPY requirements.txt .

# 2. устанавливаем Python-зависимости
RUN pip install --no-cache-dir -r requirements.txt

# ---------- application code ----------
# 3. копируем всё содержимое подпапки webui (app.py, templates/, static/…)
COPY webui/ /app

# ---------- runtime ----------
EXPOSE 8000
CMD ["python", "app.py"]
