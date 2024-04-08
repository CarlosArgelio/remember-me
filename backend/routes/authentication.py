from fastapi import APIRouter

users = APIRouter()


@users.post("/auth/sign-in", tags=["users"])
async def sign_in():
    return {'login': 'success'}

@users.post("/auth/sign-up", tags=["users"])
async def sign_in():
    return {'register': 'success'}

@users.post("/auth/forgot-password", tags=["users"])
async def sign_in():
    return {'login': 'success'}

@users.post("/auth/change-password", tags=["users"])
async def sign_in():
    return {'login': 'success'}
