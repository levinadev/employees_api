# Employees API

REST API для получения списка сотрудников с поддержкой пагинации, сортировки и фильтрации.

## Возможности API

- Получение списка сотрудников
- Пагинация
- Сортировка по любому полю
- Фильтрация по:
  - Имени
  - Email
  - Компании
  - Должности
  - Полу
  - Возрасту
  - Зарплате
  - Дате трудоустройства

## Установка и запуск локально
1. Склонируйте репозиторий:
```
git clone https://github.com/levinadev/employees_api.git
cd employees_api
```

2. Запустите сервис и базу данных в контейнерах:
```
docker compose up --build -d
```

3. После запуска документация Swagger доступна по адресу:
```
http://127.0.0.1:8000/docs
```

4. Для остановки сервисов:
```
docker compose down
```

## Запуск тестов
1. Соберите контейнеры:
```
docker compose -f docker-compose.test.yml build
```

2. Запустите тесты:
```
docker compose -f docker-compose.test.yml run tests
```

3. Для остановки сервисов:
```
docker compose -f docker-compose.test.yml down
```


## Пример запроса
Получить данные о сотруднике
```
GET /employees/?limit=5&page=1&sort=salary&order=desc&name=Slade&company=Google&gender=male
```

Ответ:
```
{
  "data": [
    {
      "name": "Slade Bowman",
      "email": "et@vitae.com",
      "age": 44,
      "company": "Google",
      "join_date": "2013-02-10T00:27:48-08:00",
      "job_title": "manager",
      "gender": "male",
      "salary": 5808
    }
  ],
  "pagination": {
    "total": 1,
    "limit": 5,
    "current_page": 1,
    "last_page": 1,
    "sort": "salary",
    "order": "desc"
  }
}
```

## Технологии
- Python 3.12
- FastAPI >=0.127.0
- Pydantic >=2.12.5
- Pydantic Settings >=2.12.0
- Uvicorn >=0.40.0
- MongoDB 7
- PyMongo >=4.15.5
- Motor (async MongoDB driver)
- Pytest >=9.0.2
- Pytest-asyncio >=1.3.0
- HTTPX >=0.28.1
- Docker, Docker Compose
- uv


## Автор
- Имя: Анна
- Email: anna45dd@yandex.ru
- GitHub: https://github.com/levinadev