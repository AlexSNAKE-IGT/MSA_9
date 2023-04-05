FROM python:3.9
LABEL authors="AlexSNAKE"

RUN mkdir "books_api"

WORKDIR /books_api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /books_api

CMD uvicorn main:books_app --host 0.0.0.0 --port 80