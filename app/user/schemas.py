from pydantic import BaseModel, Field

from .enums import RoleEnum


class UserSchema(BaseModel):
    id: int = Field(default=None)
    username: str = Field(...)
    role: RoleEnum = Field(...)


class GetUserResponseSchema(BaseModel):
    access_token: str


class CreateUserRequestSchema(BaseModel):
    username: str = Field(..., description="Username")
    password: str = Field(..., description="Password")
    role: str = Field(..., description="Role")


class CreateUserResponseSchema(BaseModel):
    username: str = Field(..., description="Username")

    class Config:
        orm_mode = True
