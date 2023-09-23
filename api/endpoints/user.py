from typing import List
from fastapi import APIRouter, Depends, HTTPException

from db.dao.user import get_users
from endpoints.auth import PermissionChecker
from endpoints.schemas.user import User

router = APIRouter()

@router.get("/", dependencies=[Depends(PermissionChecker(["USER"]))], response_model=List[User])
def get_all():
    try:
        return get_users()
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"An unexpected error occurred. Report this message to support: {e}")