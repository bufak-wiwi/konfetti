from pydantic import BaseModel, Field
from pydantic import EmailStr

class LoginToken(BaseModel):
    access_token: str
    token_type: str
    id: int
    email: EmailStr
    firstname: str
    lastname: str
    status: str
    councilId: int
    birthday: str
    permissions: dict = Field(examples=[{"USER": True, "ADMIN": False, "COUNCIL": False, "ORGANIZER": True, "1": True}])

    # model_config = {
    #     "json_schema_extra": {
    #         "examples": [
    #             {
    #                 "access_token": "eyHEADER.eyPAYLOAD.VERIFY_SIGNATURE",
    #                 "token_type": "bearer",
    #                 "id": 1,
    #                 "email": "user@example.com",
    #                 "firstname": "user",
    #                 "lastname": "user",
    #                 "status": "Acitve",
    #                 "councilId": 1,
    #                 "birthday": "01.01.1999",
    #                 "permissions": {"USER": True, "ADMIN": False, "COUNCIL": False, "ORGANIZER": True, "1": True}
    #             }
    #         ]
    #     }
    # }

class TokenData(BaseModel):
    userId: str
    email: EmailStr | None
    permissions: dict