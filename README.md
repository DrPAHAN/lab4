# Лабораторная работа №4: Парсер веб-страниц с API и PostgreSQL

# Описание проекта
REST API сервис на FastAPI, который:
Парсит веб-страницы по заданному URL (извлекает заголовок, описание, длину контента).
Сохраняет результаты в базу данных PostgreSQL.
Предоставляет доступ к сохранённым данным в формате JSON.

# Установка и настройка
# 1. Клонирование и установка зависимостей
# Cоздайте виртуальное окружение
```
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
#или
venv\Scripts\activate  # Windows
```
# Установите зависимости
```
pip install -r requirements.txt
```

# 2. Настройка базы данных PostgreSQL
# Cоздайте базу данных (через терминал)
```
createdb -h localhost -U ваш_пользователь parser_db
```
# Или через psql:
```
psql -h localhost -U ваш_пользователь
> CREATE DATABASE parser_db;
> \q
```

# 3. Настройка переменных окружения
Создайте файл .env в корне проекта:
```
# .env
DATABASE_URL=postgresql://ваш_пользователь:ваш_пароль@localhost:5432/parser_db
```

Запуск проекта
```
# Запуск сервера с авто-перезагрузкой при изменении кода
uvicorn main:app --reload
```
Сервер будет доступен по адресу: http://127.0.0.1:8000

#GET / — Проверка работоспособности
```
curl http://127.0.0.1:8000
```
ответ (JSON)
```
{
  "status": "ok",
  "docs": "/docs"
}
```

#GET /parse — Парсинг страницы
Примеры запросов:
```
# Через curl
curl "http://127.0.0.1:8000/parse?url=https://example.com"

# С кодированием специального символа
curl "http://127.0.0.1:8000/parse?url=https%3A%2F%2Fexample.com%2Fpage"
```
Успешный ответ (JSON)
```
{
  "status": "success",
  "data": {
    "url": "https://example.com",
    "title": "Example Domain",
    "description": "Example Domain. This domain is for use in illustrative examples...",
    "content_length": 1256
  }
}
```

 #Получение всех записей из БД
 ```
{
  "count": 3,
  "results": [
    {
      "id": 1,
      "url": "https://example.com",
      "title": "Example Domain",
      "description": "Example Domain. This domain...",
      "content_length": 1256,
      "parsed_at": "2026-04-23T15:30:45.123456"
    },
    {
      "id": 2,
      "url": "https://httpbin.org/html",
      "title": "No title",
      "description": "",
      "content_length": 3741,
      "parsed_at": "2026-04-23T15:32:10.654321"
    }
  ]
}
```
Ответ (JSON)
```
{
  "count": 3,
  "results": [
    {
      "id": 1,
      "url": "https://example.com",
      "title": "Example Domain",
      "description": "Example Domain. This domain...",
      "content_length": 1256,
      "parsed_at": "2026-04-23T15:30:45.123456"
    },
    {
      "id": 2,
      "url": "https://httpbin.org/html",
      "title": "No title",
      "description": "",
      "content_length": 3741,
      "parsed_at": "2026-04-23T15:32:10.654321"
    }
  ]
}
```


#Структура базы данных
```
CREATE TABLE parsed_pages (
    id SERIAL PRIMARY KEY,
    url TEXT UNIQUE NOT NULL,
    title VARCHAR(500),
    description TEXT,
    content_length INTEGER,
    parsed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```


##Примеры использования
```
# 1. Парсим страницу
curl "http://127.0.0.1:8000/parse?url=https://httpbin.org/html"

# 2. Проверяем, что данные в БД
curl http://127.0.0.1:8000/data | jq '.results[0]'
```
