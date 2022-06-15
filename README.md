[![Foodgram workflow push](https://github.com/pozarnik/foodgram-project-react/actions/workflows/foodgram_workflow_push.yml/badge.svg)](https://github.com/pozarnik/foodgram-project-react/actions/workflows/foodgram_workflow_push.yml) [![Foodgram workflow merged](https://github.com/pozarnik/foodgram-project-react/actions/workflows/foodgram_workflow_merged.yml/badge.svg)](https://github.com/pozarnik/foodgram-project-react/actions/workflows/foodgram_workflow_merged.yml)
# Foodgram

***Foodgram - сайт для размещения кулинарных рецептов***

## Возможности проекта Foodgram

- Реализована регистрация пользователей через djoser
- Вход на сайт осуществляется с помощью электронной почты и пароля
- Публикация рецептов, с добавлением необходимых ингридиентов и времени приготовления
- Поиск по ингридиентам при создании рецепта
- Возможность задать теги для рецептов
- Фильтрация рецептов по тегам
- Подписка на авторов рецептов, добавление рецептов в избранное
- Добавление рецептов в корзину покупок и скачивание их списка продуктов в txt

## Особенности настройки Docker

- Проект запускается в четырех контейнерах: nginx, PostgreSQL и Django
- Обновление образа проекта в Docker Hub

## Особенности CI & CD

- Автоматический запуск тестов **flake8** при обновлении проекта
- Автоматическое обновление образа в Docker Hub **
- Автоматический деплой проекта на сервер и его запуск в Docker **

****только при мерже pull request в ветку main**

## Технологии

- Python 3.9
- Django 4.0.4
- Django REST framework 3.13.1
- PostgreSQL 14.3
- Gunicorn 20.1.0
- nginx 1.22.0
- React

## Установка и запуск проекта

Скопируйте содержимое папки **infra/** на свой сервер

```sh
scp infra/docker-compose.yaml <ваш_логин_на_сервере>@<адрес_вашего_сервера>:~/
scp infra/nginx/default.conf <ваш_логин_на_сервере>@<адрес_вашего_сервера>:~/nginx/
```

Зайдите на свой удаленный сервер и установите Docker

```sh
ssh <ваш_логин_на_сервере>@<адрес_вашего_сервера>
sudo apt install docker.io
```

В папке infra создайте файл .env и добавьте в него переменные с вашими данными:

```
HOST                  # адрес вашего удаленного сервера
USERNAME              # ваш логин на удаленном сервере
SSH_KEY               # ваш приватный ключ ssh (по умолчанию просмотр командой cat ~/.ssh/id_rsa)
PASSPHRASE            # фраза-пароль при создании ssh ключа
DOCKERHUB_USERNAME    # ваш логин на docker.com
DOCKERHUB_TOKEN       # ваш пароль на docker.com
SECRET_KEY=           # ключ для генерации хэша Django
DEBUG=                # значение Debug
ALLOWED_HOSTS=        # разрешенные хосты
DB_ENGINE=            # укажите используемую БД
DB_NAME=              # имя базы данных
POSTGRES_USER=        # логин для подключения к БД
POSTGRES_PASSWORD=    # пароль для подключения к БД (установите свой)
DB_HOST=              # название сервиса (контейнера) БД
DB_PORT=              # порт для подключения к БД 
```

## Документации проекта Foodgram

При запущенном проекте откройте ссылку в браузере:

```sh
http://localhost/api/docs/redoc.html    (если запущен на локальной машине)
http://<адрес_вашего_сервера>/swagger/
```

## Мои профили

- [GitHub](https://github.com/pozarnik/)
- [LinkedIn](https://www.linkedin.com/in/ivan-alekseyevich/)

## License

MIT



