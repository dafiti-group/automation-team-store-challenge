FROM python:3.9.1

ENV PYTHONUNBUFFERED 1
RUN mkdir /store
WORKDIR /store
COPY requirements.txt /store/
RUN pip install -r requirements.txt
COPY . /store/
