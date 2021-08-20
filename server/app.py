from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    res = {
        "status": "success",
        "body": "Welcome to this fantastic apps"
    }
    return res