from typing import List
from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from endpoints.helper.mailing.mailing import sendEmail


from db.session import get_db
from db.dao.user import get_users, create_user_in_db, get_user, create_user_secret, update_role_in_db, get_users_with_roles
from endpoints.helper.auth.authHelper import refresh_token_in_response, generate_jwt, get_hash, create_random_secret
from endpoints.auth import PermissionChecker, depend_token
from endpoints.schemas.auth import TokenData
from endpoints.schemas.user import ShowUser, CreateUser, UpdateUser
from endpoints.schemas.usersecret import UserSecret
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
def get_all(db: Session = Depends(get_db), current_user: TokenData = Depends(depend_token)):
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

"""Endpoint to create a new user

Parameters:
    user2create (CreateUser): body parameters for new user

Returns:
    HTTP: 201 Created or 409 Conflict if duplicate email
"""
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user2create: CreateUser, request: Request, db: Session = Depends(get_db)):
    new_user = create_user_in_db(user2create, db)
    if new_user:
        expiration_time = timedelta(days=7)
        register_token = generate_jwt({"sub": str(new_user.id),
                                       "email": new_user.email}, 
                                       expires_delta=expiration_time)
        
        valid_until = datetime.utcnow() + expiration_time
        secret_to_create = UserSecret(userId=new_user.id, 
                                      password=get_hash(create_random_secret()), 
                                      registrationToken = register_token, 
                                      registrationTokenValidUntil = valid_until)
        new_secret = create_user_secret(secret_to_create, db)
        #TODO change template for dev env on server and handle valid link
        return sendEmail(template="userRegistration",to=new_user.email, subj="Willkommen in Konfetti",
                  fields={"name":new_user.firstname,
                          "setPasswdUrl":f"{request.base_url}reset-password/{new_secret.registrationToken}"})
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
@router.put("/{userId}", dependencies=[Depends(PermissionChecker(["USER" or "ADMIN"]))])
def update_user(user2update: UpdateUser, userId: int, db: Session = Depends(get_db), current_user: TokenData = Depends(depend_token)):
    pass

#TODO: object handling from frontend
@router.put("/{userId}/role", dependencies=[Depends(PermissionChecker(["ADMIN"]))])
def update_user_role(userId: int, roledId: int, councilId: int, db: Session = Depends(get_db)):
    pass

#TODO: Admin permission doesnt work yet, 
#TODO: scheme
@router.get("/", dependencies=[Depends(PermissionChecker(["USER"]))]) 
def get_all_with_roles(db: Session = Depends(get_db), current_user: TokenData = Depends(depend_token)):
    pass