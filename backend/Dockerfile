FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt --no-cache-dir

CMD ["gunicorn", "backend.wsgi:application", "--bind", "0:8000" ]

RUN python manage.py makemigrations

RUN python manage.py migrate

RUN python manage.py collectstatic --no-input