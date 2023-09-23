from pydantic import BaseModel
from pydantic import EmailStr


class User(BaseModel):
    id: int
    email: EmailStr
    status: str

    class Config:  # tells pydantic to convert even non dict obj to json
        orm_mode = True