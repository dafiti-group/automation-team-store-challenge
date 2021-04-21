# FROM nginx

# RUN rm /etc/nginx/conf.d/default.conf
# COPY nginx.conf /etc/nginx/conf.d

FROM redis:alpine
WORKDIR /redis
COPY redis.conf /usr/local/etc/redis/redis.conf

# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/automation-team-store-challenge/dafitishoes

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN apk add --no-cache --upgrade bash

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/automation-team-store-challenge/dafitishoes/entrypoint.sh"]