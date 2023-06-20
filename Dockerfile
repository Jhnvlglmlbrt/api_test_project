# Указываем базовый образ
FROM python:3.9

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем требования проекта в контейнер

COPY requirements.txt ./

# Устанавливаем зависимости проекта
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта в контейнер
COPY . .

# Указываем команду запуска приложения

ENTRYPOINT ["pytest", "-s", "-v", "--junit-xml", "/test_result.xml"]

# Добавьте команду запуска в README:
# Запуск контейнера:
# docker build -t test-api .
# docker run -it --rm test-api