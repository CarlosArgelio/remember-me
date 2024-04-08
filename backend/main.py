from fastapi import FastAPI
from routes.users import users

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(users)
