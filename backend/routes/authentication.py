from fastapi import APIRouter, status

auth = APIRouter(
    prefix='/auth'
)


@auth.post("/sign-in")
async def sign_in():
    return {'login': 'success'}

@auth.post("/sign-up", status_code=status.HTTP_201_CREATED)
async def sign_up():
    return {'register': 'success'}

@auth.post("/forgot-password")
async def forgot_pasword():
    return {'login': 'success'}

@auth.post("/change-password")
async def change_password():
    return {'login': 'success'}
