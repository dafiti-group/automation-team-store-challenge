#!/bin/sh

echo "Waiting for postgres..."

while ! $(nc -z db 5432); do
    sleep 0.1
done

python manage.py makemigrations
python manage.py migrate

echo "------PostgreSQL started-------"

python manage.py collectstatic --no-input

gunicorn dafitishoes.wsgi:application --bind :8000 --workers=3 --reload

exec "$@"