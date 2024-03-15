from typing import Union
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI

from src.book_examples import ExampleBookData





app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def read_root():
    return {"Hello": "World"}



# ===== User ===== #
@app.post("/register")
def register_user():
    return {"Sign up successfull!"}


@app.post("/login")
def register_user():
    return {"Login successfull!"}


# ===== Books ===== #
@app.get("/recommendations")
def get_reccomendations():
    return ExampleBookData

@app.get("/search_history")
def get_reccomendations():
    return ExampleBookData

@app.get("/bookmarks")
def get_reccomendations():
    return ExampleBookData

@app.post("/search_image")
def search_image():
    return ExampleBookData[0]

@app.get("/search_text/{text}")
def search_text():
    return ExampleBookData[0]