from fastapi import FastAPI
from starlette import status
from starlette.responses import Response

app = FastAPI()


@app.get('/')
def root():
    return {'message': 'Hello World'}