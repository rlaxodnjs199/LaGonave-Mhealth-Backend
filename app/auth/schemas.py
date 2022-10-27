from pydantic import BaseModel, Field

from .enums import RoleEnum


class UserSchema(BaseModel):
    id: int = Field(default=None)
    username: str = Field(...)
    password: str = Field(...)
    role: RoleEnum = Field(...)
