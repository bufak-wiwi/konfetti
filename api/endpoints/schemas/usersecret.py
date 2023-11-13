from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from pydantic import EmailStr

class ResetUser(BaseModel):
    password: str


class UserSecret(BaseModel):
    userId: int
    password: str
    registrationToken: str
    registrationTokenValidUntil: datetime

class UpdateToken(BaseModel):
    userId: int
    registrationToken: str
    registrationTokenValidUntil: datetime

    class Config:  # tells pydantic to convert even non dict obj to json
        orm_mode = True