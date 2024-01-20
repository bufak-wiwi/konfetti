from pydantic import BaseModel

class Council(BaseModel):
    id: int
    name: str
    university: str
    city: str