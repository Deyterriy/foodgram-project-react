![foodgram-project-react Workflow Status](https://github.com/deyterriy/foodgram-project-react/actions/workflows/main.yml/badge.svg)
# Продуктовый помощник Foodgram 


[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=56C0C0&color=008080)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=56C0C0&color=008080)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat&logo=NGINX&logoColor=56C0C0&color=008080)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat&logo=gunicorn&logoColor=56C0C0&color=008080)](https://gunicorn.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/)
[![Docker-compose](https://img.shields.io/badge/-Docker%20compose-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/)
[![Docker Hub](https://img.shields.io/badge/-Docker%20Hub-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)](https://www.docker.com/products/docker-hub)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat&logo=GitHub%20actions&logoColor=56C0C0&color=008080)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat&logo=Yandex.Cloud&logoColor=56C0C0&color=008080)](https://cloud.yandex.ru/)

## Описание проекта Foodgram
«Фудграм» — сайт, на котором пользователи публикуют рецепты, добавляют 
рецепты других пользователей в избранное и подписываются на публикации других авторов. 
Пользователям сайта также доступен сервис «Список покупок». 
Он позволяет создавать список продуктов в txt-формате, которые нужно купить для приготовления выбранных блюд. 

## Запуск проекта в dev-режиме

- Клонируйте репозиторий с проектом на свой компьютер. В терминале из рабочей директории выполните команду:
```bash
git clone <https or SSH URL>
```

- Установить и активировать виртуальное окружение

```bash
source /venv/Scripts/Activate
```

- Установить зависимости из файла requirements.txt

```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

### Выполните миграции:
```bash
python manage.py migrate
```

- В папке с файлом manage.py выполнить команду:
```bash
python manage.py runserver
```

- Создание нового супер пользователя 
```bash
python manage.py createsuperuser
```

### Загрузите статику:
```bash
docker compose exec backend python manage.py collectstatic
docker compose exec backend cp -r /app/static/. web/static
```
### Заполните базу тестовыми данными: 
```bash
python manage.py load_ingredients_data 
```


Для развертывания на удаленном сервере необходимо клонировать репозиторий на 
локальную машину. Подготовить и загрузить образы на Docker Hub.

Клонировать репозиторий:
```shell
git clone <https or SSH URL>
```

Перейти в каталог проекта:
```shell
cd foodgram
```

Создать .env:
```shell
touch .env
```

Шаблон содержимого для .env файла:
```shell
# Django settings
DEBUG=False
SECRET_KEY=<django_secret_key>
ALLOWED_HOSTS=127.0.0.1, localhost, <example.com, xxx.xxx.xxx.xxx>

# DB
POSTGRES_DB=foodgram
POSTGRES_USER=foodgram_user
POSTGRES_PASSWORD=foodgram_password
DB_NAME=foodgram
DB_HOST=db
DB_PORT=5432

# Docker images
BACKEND_IMAGE=<username>/foodgram_back
FRONTEND_IMAGE=<username>/foodgram_front
GATEWAY_IMAGE=<username>/foodgram_gate
```

Создать docker images образы:
```shell
sudo docker build -t <username>/foodgram_back
sudo docker build -t <username>/foodgram_front
sudo docker build -t <username>/foodgram_gate
```

Загрузить образы на Docker Hub:
```shell
sudo docker push <username>/foodgram_back
sudo docker push <username>/foodgram_front
sudo docker push <username>/foodgram_gateway
```

Создать на сервере папку `foodgram` 
```shell
mkdir /home/<username>/foodgram
```

Перенести на удаленный сервер файлы`.env` и `docker-compose.yml`.
```shell
scp .env docker-compose.yml <username>@<server_address>:/home/<username>/foodgram
```

Подключиться к серверу:
```shell
ssh <username>@<server_address>
```

Перейти в директорию `foodgram`:
```shell
cd /home/<username>/foodgram
```

Выполнить сборку приложений:
```shell
sudo docker compose up -d
```

Выполнить заполнение базы ингредиентами:
```shell
docker compose exec backend python manage.py load_ingredients_data
```

## GitHub Actions
Для использования автоматизированного развертывания и тестирования нужно 
изменить `.github/workflows/main.yml` под свои параметры и задать Actions secrets
в репозитории.

Actions secrets:
- `secrets.DOCKER_USERNAME`
- `secrets.DOCKER_PASSWORD`
- `secrets.HOST`
- `secrets.USER`
- `secrets.SSH_KEY`
- `secrets.SSH_PASSPHRASE`
- `secrets.TELEGRAM_TO`
- `secrets.TELEGRAM_TOKEN`

Данные для доступа:
- login - admin@admin.com
- pass - admin