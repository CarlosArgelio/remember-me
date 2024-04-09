from fastapi import APIRouter
from schemas.users import UserSignUp
from controllers.users import UserController

users = APIRouter()


@users.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

@users.get("/users/me", tags=["users"])
async def read_my_user():
    return {"username": "Rick"}

@users.post("/users/", tags=["users"])
async def create_user(payload: UserSignUp):
    controller = UserController()
    payload = payload.model_dump()
    new_user = controller.create_user(payload)
    return new_user
    

@users.patch("/users/{id}", tags=["users"])
async def update_user(id):
    return {"username": "Rick"}

@users.delete("/users/", tags=["users"])
async def delete_user():
    return ''