from typing import List
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str


class Author(BaseModel):
    name: str

class Book(BaseModel):
    title: str
    authors: List[Author]
    description_short: str
    image_url: str
    isbn: str