from datetime import date, datetime
import re
from uuid import UUID

from pydantic import BaseModel, Field, validator


class CreatePatientRequestSchema(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    birth_date: date = Field(...)
    gender: str = Field(...)
    height: float = Field(...)
    weight: float = Field(...)
    phone_number: str = Field(...)
    recorder_id: str = Field(...)

    @validator("birth_date", pre=True)
    def parse_birth_date(cls, value):
        return datetime.strptime(value, "%m/%d/%Y").date()

    @validator("phone_number")
    def validate_phone_number(cls, value):
        if re.match(r"[0-9]+", value) and len(value) == 10:
            return value
        else:
            raise ValueError("Phone number must be number only and length of 10")


class CreatePatientResponseSchema(BaseModel):
    id: UUID = Field(...)
    full_name: str = Field(...)

    class Config:
        orm_mode = True


class GetPatientResponseSchema(BaseModel):
    id: UUID = Field(...)
    full_name: str = Field(...)

    class Config:
        orm_mode = True
