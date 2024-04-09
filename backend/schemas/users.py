from pydantic import BaseModel, EmailStr

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

class UserSignUp(BaseModel):
    email: EmailStr
    password: str