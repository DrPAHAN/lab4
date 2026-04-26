# Лабораторная работа №4: Парсер веб-страниц с API и PostgreSQL

# Описание проекта
REST API сервис на FastAPI, который:
Парсит веб-страницы по заданному URL (извлекает заголовок, описание, длину контента)
Сохраняет результаты в базу данных PostgreSQL
Предоставляет доступ к сохранённым данным в формате JSON

# Установка и настройка
# 1. Клонирование и установка зависимостей
# Создайте виртуальное окружение (рекомендуется)
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
# Создайте базу данных (через терминал)
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
