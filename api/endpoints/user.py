from typing import List
from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from endpoints.helper.mailing.mailing import sendEmail


from db.session import get_db
from db.dao.user import get_users, create_user_in_db, get_user, create_user_secret
from endpoints.helper.auth.authHelper import encode_jwt, refresh_token_in_response, generate_jwt, get_hash, create_random_secret
from endpoints.auth import PermissionChecker, depend_token
from endpoints.schemas.auth import TokenData
from endpoints.schemas.user import ShowUser, CreateUser, UpdateUser
from endpoints.errorhandler import errorhandler
from db.session import get_db
from sqlalchemy.orm import Session

from db.models.userSecret import UserSecret


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
        valid_until_date = datetime.now() + timedelta(days=7)
        register_token = generate_jwt({"sub": str(new_user_id),"email": get_user(new_user_id, db).email, "exp": valid_until_date})
        secret_to_create = UserSecret(userId=new_user_id, password=get_hash(create_random_secret()), registrationToken = register_token, registrationTokenValidUntil = valid_until_date)
        valid_token = create_user_secret(secret_to_create, db)
        # sendEmail(template="sample",to="testreciupient@test.local", subj="Testmail", replyTo="testeplytp@test.local",fields={"name":"Konfetti User","message":"Thank you for using our system. Have fun."})

        return valid_token #TODO send register email with valid token
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
def update_user(user2update: UpdateUser, id: int, db: Session = Depends(get_db), current_user: TokenData = Depends(depend_token
)):
    pass