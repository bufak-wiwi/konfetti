from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder


from db.session import get_db
from db.dao.user import get_users
from endpoints.auth import PermissionChecker, get_current_user, refresh_token_in_response
from endpoints.schemas.auth import TokenData
from endpoints.schemas.user import ShowUser, CreateUser, UpdateUser
from endpoints.errorhandler import errorhandler

router = APIRouter()

"""Endpoint to return all user
Persmissions: User

Returns:
    HTTP: JSON representation of list of all user, each represented by the schema ShowUser
"""
@router.get("/", dependencies=[Depends(PermissionChecker(["USER"]))], response_model=List[ShowUser])
def get_all(db: Session = Depends(get_db), current_user: TokenData = Depends(get_current_user)):
    try:
        all_users = get_users(db)

        all_showusers = [ShowUser(id=user.id, email=user.email, status=user.status) for user in all_users] #should be possible automatically

        return refresh_token_in_response(JSONResponse(jsonable_encoder(all_showusers)), current_user)
    except Exception as ex:
        errorhandler(ex)

"""Endpoint to return one user identified by id

Parameters:
    id (int): id of the user to return

Returns:
    HTTP: JSON representation of one user, represented by the schema ShowUser
""" 
@router.get("/{id}", dependencies=[Depends(PermissionChecker(["USER"]))], response_model=ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    pass

"""Endpoint

Parameters:
    user2create (CreateUser): [description]

Returns:
    HTTP: 
"""
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user2create: CreateUser, db: Session = Depends(get_db)):
    pass

"""Endpoint

Parameters:
    user2update (UpdateUser): [description]
    id (int): [description]

Returns:
    HTTP: 
"""
@router.put("/{id}", dependencies=[Depends(PermissionChecker(["USER"]))])
def update_user(user2update: UpdateUser, id: int, db: Session = Depends(get_db), current_user: TokenData = Depends(get_current_user)):
    pass