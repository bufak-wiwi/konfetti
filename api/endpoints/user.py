from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder


from db.session import get_db
from db.dao.user import get_users, create_user_in_db, get_user, create_user_secret
from endpoints.auth import PermissionChecker, get_current_user, refresh_token_in_response
from endpoints.schemas.auth import TokenData
from endpoints.schemas.user import ShowUser, CreateUser, UpdateUser
from endpoints.errorhandler import errorhandler
from db.session import get_db
from sqlalchemy.orm import Session


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
def get_specific_user(id: int, db: Session = Depends(get_db)):
    return get_user(id, db)

"""Endpoint

Parameters:
    user2create (CreateUser): [description]

Returns:
    HTTP: 
"""
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user2create: CreateUser, db: Session = Depends(get_db)):
    new_user_id = create_user_in_db(user2create, db)
    if new_user_id:
        return True
        # TODO: create_user_secret(new_user_id, db) #either with pw from user entry or with placeholder
    else: 
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with email already exists",
        )


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