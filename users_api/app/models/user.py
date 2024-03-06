from enum import Enum
from pydantic import BaseModel


class User(BaseModel):
    login: str
    age: int