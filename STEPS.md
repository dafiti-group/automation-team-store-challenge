Stack:
Docker and Docker Compose
Django
Django Rest Framework
Gunicorn
PostgreSQL

Populate Database

docker exec -it <container ID> python manage.py loaddata women_shoes/fixtures/women_shoes.json
