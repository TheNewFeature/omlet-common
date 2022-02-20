from typing import Optional

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int
    name: str
    username: str
    email: EmailStr
    password: Optional[str]

    class Config:
        orm_mode = True


class CreateUserRequest(BaseModel):
    name: str
    username: str
    email: EmailStr
    password: str


class CreateUserResponse(BaseModel):
    user: Optional[User]
