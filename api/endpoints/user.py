from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, responses

from db.dao.user import get_users, create_user_in_db, get_user, create_user_secret
from endpoints.auth import PermissionChecker, get_current_user, refresh_access_token
from endpoints.schemas.auth import TokenData
from endpoints.schemas.user import ShowUser, CreateUser, UpdateUser
from endpoints.errorhandler import errorhandler
from db.session import get_db
from sqlalchemy.orm import Session


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
    
@router.get("/{id}", response_model=ShowUser)
def get_specific_user(id: int, db: Session = Depends(get_db)):
    return get_user(id, db)
    
    
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user2create: CreateUser, db: Session = Depends(get_db)):
    new_user_id = create_user_in_db(user2create, db)
    if new_user_id:
        return True
        # create_user_secret(new_user_id, db) #either with pw from user entry or with placeholder
    else: 
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with email already exists",
        )


@router.put("/{id}", dependencies=[Depends(PermissionChecker(["USER"]))])
def update_user(user2update: UpdateUser, id: int, current_user: TokenData = Depends(get_current_user)):
    pass