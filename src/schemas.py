from datetime import datetime, date
from pydantic import BaseModel, Field, EmailStr

class ResponseModel(BaseModel):
    id: int
    first_name: str = Field(max_length=25)
    last_name: str = Field(max_length=25)
    email: EmailStr = Field(max_length=120)
    birthday: date
    description: str | None = None

    class Config:
        from_attributes = True

class ContactModel(BaseModel):
    first_name: str = Field(max_length=25)
    last_name: str = Field(max_length=25)
    email: EmailStr = Field(max_length=120)
    birthday: date
    description: str | None = None

    class Config:
        from_attributes = True