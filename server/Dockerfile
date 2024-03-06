FROM ubuntu:latest
FROM python:latest
LABEL authors="danilabondarenko"

WORKDIR /server

EXPOSE 90

COPY ./app /server/app

CMD ["python3", "/server/app/main.py"]