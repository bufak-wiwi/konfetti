from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, responses

from db.dao.user import get_users
from endpoints.auth import PermissionChecker, get_current_user, refresh_access_token
from endpoints.schemas.auth import TokenData
from endpoints.schemas.user import ShowUser, CreateUser, UpdateUser
from endpoints.errorhandler import errorhandler

router = APIRouter()

# to refresh the token set the Response to
# response.set_cookie(key="access_token", value=f"Bearer {refresh_access_token()}", httponly=True)

@router.get("/", dependencies=[Depends(PermissionChecker(["USER"]))], response_model=List[ShowUser])
def get_all():
    try:
        all_users = get_users()
        response = responses.Response(all_users)
        response.set_cookie(key="access_token", value=f"Bearer {refresh_access_token()}", httponly=True)
        return response
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