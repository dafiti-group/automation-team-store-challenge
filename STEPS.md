# Welcome to Dafiti Women Shoes

---

## Stack:
<ul>
    <li>Docker 20.10.2</li>
    <li>Docker Compose 1.28.5</li>
    <li>Django 3.2</li>
    <li>Django REST Framework 3.12</li>
    <li>Gunicorn 20.0.4</li>
    <li>PostgreSQL 13.2</li>
    <li>Redis 3.4.1</li>
    <li>Celery 4.4.1</li>
    <li>Python 3.8.3</li>
</ul>

---

## How to build:

Download the content of this repository, then go inside <strong>dafiti_shoes</strong> folder and run <pre>docker-compose up --build</pre> and after you hit Enter all should be set. Enjoy a cup of coffee while Docker does the work.

---

## Populate Database:

After everything is up and running, list your containers with <pre>docker container ls</pre> and get the ID from the container which has the <strong>web</strong> service in it. It should be called "dafitishoes_web" or similar. After that, run the following comand to load the fixture file inside PostgreSQL:
<pre>docker exec -it #container ID# python manage.py loaddata women_shoes/fixtures/women_shoes.json</pre>
It should populate nearly 1041 rows.

The data for this fixture was extracted from Kaggle free datasets.

---

## URLs

#### women_shoes/list/

Lists all women shoes. Supports GET, POST, HEAD, OPTIONS.

#### women_shoes/detail/<int:pk>/

List a particular shoe through it's ID. Supports GET, PUT, PATCH, DELETE, HEAD, OPTIONS.

---

## Frontend

Frontend for this application is offered by Django REST Application.