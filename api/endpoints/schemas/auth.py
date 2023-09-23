from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str
    userId: int
    role: int

class TokenData(BaseModel):
    userId: int
    permissions: dict