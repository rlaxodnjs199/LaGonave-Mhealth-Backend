from datetime import date, datetime

from pydantic import BaseModel, Field, validator


class CreatePatientRequestSchema(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    birth_date: date = Field(...)
    gender: str = Field(...)
    height: float = Field(...)
    weight: float = Field(...)
    phone_number: str = Field(...)
    user_id: str = Field(...)

    @validator("birth_date", pre=True)
    def parse_birth_date(cls, value):
        return datetime.strptime(value, "%m/%d/%Y").date()
