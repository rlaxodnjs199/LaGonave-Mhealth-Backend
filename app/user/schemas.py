from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, Field

from .enums import RoleEnum


class UserSchema(BaseModel):
    id: UUID = Field(...)
    username: str = Field(...)
    role: RoleEnum = Field(...)


class LoginResponseSchema(BaseModel):
    access_token: str
    user_id: UUID = Field(...)


class GetUserResponseSchema(BaseModel):
    username: str = Field(...)
    role: RoleEnum = Field(...)
    created_at: datetime = Field(...)
    updated_at: datetime = Field(...)

    class Config:
        orm_mode = True


class CreateUserRequestSchema(BaseModel):
    username: str = Field(..., description="Username")
    password: str = Field(..., description="Password")
    role: str = Field(..., description="Role")


class CreateUserResponseSchema(BaseModel):
    username: str = Field(..., description="Username")

    class Config:
        orm_mode = True
