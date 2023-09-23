from pydantic import BaseModel
from pydantic import EmailStr


class UserLogin(BaseModel):
    email: EmailStr

class ShowUser(BaseModel):
    id: int
    email: EmailStr

    class Config:  # tells pydantic to convert even non dict obj to json
        orm_mode = True