from fastapi import FastAPI
from routes.users import users

from database.config import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(users)
