# project/app/main.py


from fastapi import FastAPI, Depends
from app.config import get_settings, Settings

app = FastAPI()


@app.get("/ping")
def pong():
    return {"ping": "pong!"}

@app.get("/hello_world")
async def hello_world():
    return {"message": "Hello World"}


@app.get("/polak")
async def polak():
    return {"Bossman": "POLAK"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.get("/items_int/{item_id}")
async def read_item_int(item_id: int):
    return {"item_id": item_id}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/ping_test")
def pong_test(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }


@app.get("/docker_test")
def docker_test(settings: Settings = Depends(get_settings)):
    return {
        "ping": "docker-pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }