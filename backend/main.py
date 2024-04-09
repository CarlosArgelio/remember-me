from fastapi import FastAPI
from routes.users import users
from routes.reminders import reminders
from routes.authentication import auth

from database.config import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(auth, prefix="/api/v1", tags=["auth"])
app.include_router(users, prefix="/api/v1", tags=["users"])
app.include_router(reminders, prefix="/api/v1", tags=["reminders"])
