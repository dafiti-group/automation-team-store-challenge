FROM python:3.6

ARG WORKERS=4
ARG THREADS=4

COPY requirements.txt requirements-dev.txt /opt/
COPY wait_db_to_start_server.py manage.py /opt/
COPY src /opt/src
COPY clothing_manager /opt/clothing_manager

WORKDIR /opt/

RUN pip install --use-feature=2020-resolver -r /opt/requirements.txt \
    pip install --use-feature=2020-resolver -r /opt/requirements-dev.txt

ENV DB_NAME=clothing_manager \
    DB_USER=root \
    DB_PASS=password \
    DB_SERVICE=db \
    DB_HOST="db" \
    DB_PORT=3306
