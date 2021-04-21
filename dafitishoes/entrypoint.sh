#!/bin/sh

echo "Waiting for postgres..."

while ! $(nc -z db 5432); do
    sleep 0.1
done

echo "------PostgreSQL started-------"

if [[ $ONLY_CELERY = "FALSE" ]]
then
    python manage.py makemigrations
    python manage.py migrate
    python manage.py collectstatic --no-input

else
    while true; do
        sleep 1
    done
fi

gunicorn dafitishoes.wsgi:application --bind 0.0.0.0:8000 --workers=3 --reload

exec "$@"