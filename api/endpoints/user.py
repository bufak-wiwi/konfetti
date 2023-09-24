from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from db.dao.user import get_users
from endpoints.auth import PermissionChecker, get_current_user
from endpoints.schemas.auth import TokenData
from endpoints.schemas.user import ShowUser, CreateUser, UpdateUser
from endpoints.errorhandler import errorhandler

router = APIRouter()

@router.get("/", dependencies=[Depends(PermissionChecker(["USER"]))], response_model=List[ShowUser])
def get_all():
    try:
        return get_users()
    except Exception as ex:
        errorhandler(ex)
    
@router.get("/{id}", dependencies=[Depends(PermissionChecker(["USER"]))], response_model=ShowUser)
def get_user(id: int):
    pass
    
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user2create: CreateUser):
    pass

@router.put("/{id}", dependencies=[Depends(PermissionChecker(["USER"]))])
def update_user(user2update: UpdateUser, id: int, current_user: TokenData = Depends(get_current_user)):
    pass