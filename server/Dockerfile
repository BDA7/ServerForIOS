FROM ubuntu:latest
FROM python:latest
LABEL authors="danilabondarenko"

WORKDIR /server

COPY ./requirements.txt /server/requirements.txt
COPY ./app /server/app

RUN pip install --no-cache-dir --upgrade -r /server/requirements.txt

CMD ["uvicorn", "app.web_socket:app", "--host", "0.0.0.0", "--port", "90"]