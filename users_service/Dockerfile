FROM python:3.9
LABEL authors="AlexSNAKE"

RUN mkdir "users_api"

WORKDIR /users_api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /users_api

CMD uvicorn main:users_app --host 0.0.0.0 --port 80
