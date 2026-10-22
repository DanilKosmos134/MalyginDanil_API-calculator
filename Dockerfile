# 1. Берем официальный легкий образ Python
FROM python:3.11-slim

# 2. Создаем рабочую директорию внутри контейнера
WORKDIR /app

# 3. Сначала копируем только файл с зависимостями
COPY requirements.txt .

# 4. Устанавливаем библиотеки (этот шаг кэшируется, чтобы сборка шла быстрее)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Копируем весь остальной код проекта
COPY . .

# 6. Создаем отдельного пользователя
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# 7. Сообщаем, какой порт будет использовать контейнер
EXPOSE 8000

# 8. Команда для запуска. Важно: используем 0.0.0.0, чтобы к API можно было обратиться снаружи
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]