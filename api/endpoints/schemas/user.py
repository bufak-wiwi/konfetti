from typing import Optional
from pydantic import BaseModel
from datetime import date
from pydantic import EmailStr

# Representationschema for the requestbody to create a user
class CreateUser(BaseModel):
    email: EmailStr
    firstname: str
    lastname: str
    councilId: int
    birthday: date | None

# Representationschema for the requestbody to update a user
class UpdateUser(BaseModel):
    id: int
    email: EmailStr
    firstname: str
    lastname: str
    councilId: int
    birthday: date | None

# Representationschema for the responsebody to display a user
class ShowUser(BaseModel):
    id: int
    email: EmailStr
    status: str

    class Config:  # tells pydantic to convert even non dict obj to json
        orm_mode = True