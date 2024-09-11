# Используйте официальный Python образ
FROM python:3.10-slim

# Установите рабочую директорию
WORKDIR /storage

# Скопируйте содержимое текущего каталога в контейнер
COPY . /storage

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Откройте порт 5000
EXPOSE 5000

# Запустите приложение
CMD ["python", "log_service.py"]
