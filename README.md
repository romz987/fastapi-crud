# Task Manager

Менеджер задач(Task Manager) - простое приложение, написанное в качестве тестового задания на предложение по работе.

Стек:

- FastAPI
- SQLAlchemy
- PostgreSQL
- Pytest
- Docker

## Table of Contents

- [Features](#Features)
- [Project Structure](#Project-Structure)
- [Usage](#Usage)
- [API Endpoints](#API-Endpoints)

## Features

- Базовые CRUD-операций
- Отдельная операция для обновления статуса задачи (?)
- Простая структура проекта
- Swagger UI

## Project Structure

```
task-manager
.
├──   alembic
│   ├──  env.py
│   ├──   README
│   ├──  script.py.mako
│   └──   versions
├── alembic.ini
├──   app
│   ├──  context_manager.py
│   ├──  crud.py
│   ├──   db
│   │   ├──  database.py
│   │   └──  models.py
│   ├──  main.py
│   └──  schemas.py
├──  env.sample
├──   pyproject.toml
├──   README.md
├──  requirements.txt
└──   tests
    └──  test_crud.py
```

- app: Директория содержит основной код приложения
  - context_manager.py: Контекстный менеджер (для подключения работы с базой данных)
  - main.py: Точка входа и routes
  - schemas.py: Схемы валидации pydantic
  - crud.py: Логика работы с БД (базовые CRUD-операции)
  - db:
    - database.py: Настройки подключения к базе данных
    - models.py: Файл с моделью тудушки
- alembic: Директория конфигурации alembic и файлы миграции
- tests: unit-тесты
- env.sample: Пример структуры файла .env
- pyproject.toml: Конфигурации проекта
- requirements.txt: Файл с зависимостями
- README.md: Текущий READMEfile

## Usage

## API Endpoints
