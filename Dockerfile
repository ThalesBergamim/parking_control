FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


EXPOSE 8000
