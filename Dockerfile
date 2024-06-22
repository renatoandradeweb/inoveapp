# Dockerfile

FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY app/requirements.txt /app/

RUN apt-get update && apt-get install -y netcat-openbsd

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY app /app/
