# FastAPI API for Loading and Serving the Model

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    return {"Hello": "World"}  