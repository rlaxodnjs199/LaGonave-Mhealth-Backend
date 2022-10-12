from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    id: int = Field(default=None)
    username: str = Field(...)
    password: str = Field(...)
