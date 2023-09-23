from fastapi import APIRouter

from db.dao.user import get_user_by_email
from db.models.user import User
from endpoints.schemas.user import ShowUser
from endpoints.schemas.user import UserLogin

router = APIRouter()

@router.get("/test")
def test():
    return {"message": f"Hello from the otherside"}

@router.post("/login", response_model=ShowUser)
def login(user: UserLogin):
    rp_user = get_user_by_email(email=user.email)
    print(rp_user)
    if not rp_user:
        return False
    return rp_user