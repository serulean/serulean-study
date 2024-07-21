from typing import Optional, List
from beanie import Document, Link
from pydantic import BaseModel, EmailStr
from models.events import Event


class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Event]]

    class Settings:
        name = "users"

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "username": "strong!!!",
                "events": []
            }
        }


# class UserSignIn(BaseModel):
#     email: EmailStr
#     password: str


class ToeknResponse(BaseModel):
    access_token: str
    token_type: str
