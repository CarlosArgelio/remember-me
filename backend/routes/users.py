from fastapi import APIRouter, status
from schemas.users import UserSignUp
from controllers.users import UserController

users = APIRouter(
    prefix="/users",
)


@users.get("/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

@users.get("/me")
async def read_my_user():
    return {"username": "Rick"}

@users.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(payload: UserSignUp):
    controller = UserController()
    payload = payload.model_dump()
    new_user = controller.create_user(payload)
    return new_user


@users.patch("/{id}")
async def update_user(id):
    return {"username": "Rick"}

@users.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user():
    pass
