FROM python:latest
LABEL authors="danilabondarenko"

WORKDIR /users_api

COPY ./requirements.txt /users_api/requirements.txt
COPY ./app /users_api/app

RUN pip install --no-cache-dir --upgrade -r /users_api/requirements.txt

CMD ["uvicorn", "app.users_api:app", "--host", "0.0.0.0", "--port", "80"]