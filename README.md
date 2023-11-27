# Library_DRF

API for library(Django, DRF, Celery, Redis &amp; Docker)

## Установка

1. Скачайте проект в домашнюю директорию.
2. Активируйте виртуальное окружение командой: poetry shell.
3. Установите зависимости командой: poetry install.

## Перед первым запуском программы:

Создайте Базу данных (в данной работе используется PostgreSQL) и перейдите в файл .env.sample и пропишите переменные
окружения в формате(все данные после "=" в виде примера):

```ini
SECRET_KEY = 'django-secret-key'
DEBUG = True/False

POSTGRES_DB = 'name_of_db'
POSTGRES_USER = 'db_user'
POSTGRES_PASSWORD = 'your_password'
POSTGRES_HOST = 'db'
POSTGRES_PORT = 5432

CELERY_BROKER_URL = 'smth://123.1.1.0:1234/0'
CELERY_RESULT_BACKEND = 'smth://123.1.1.0:1234/0'
CELERY_TIMEZONE = 'UTC'

EMAIL_HOST=email.host.com
EMAIL_PORT=465
EMAIL_HOST_USER=ur_mail@gmail.com/ru
EMAIL_HOST_PASSWORD=your_password
EMAIL_USE_TLS=True/False
EMAIL_USE_SSL=True/False

```

***

## Работа кода

Выполните команду ```docker-compose up -d --build```

## Для завершения работы

В терминале, где запущен docker, выполните команду ```docker-compose down```








