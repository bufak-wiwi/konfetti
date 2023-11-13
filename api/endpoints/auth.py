from datetime import datetime, timedelta
from typing import Annotated, List
from fastapi import Depends, APIRouter, HTTPException, Request, status, responses
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from db.session import get_db
from db.dao.user import get_user, get_user_for_login, get_userpermission, get_user_status, get_user_by_email, update_token, update_user_secret
from endpoints.schemas.auth import LoginToken, TokenData
from endpoints.schemas.user import ShowUser
from endpoints.schemas.usersecret import ResetUser, UserSecret, UpdateToken
from endpoints.helper.auth.authHelper import generate_jwt, verify_password, decode_jwt, oauth2_scheme, get_hash, get_reset_token, create_random_secret
from endpoints.helper.mailing.mailing import sendEmail

router = APIRouter()

def authenticate(username: str, password: str, db: Session):
    user_secrect = get_user_for_login(username, db = db)
    if not user_secrect:
        return False
    if not verify_password(password, user_secrect.password):
        return False
    return get_user(user_secrect.userId, db)  

def depend_token(token: Annotated[str, Depends(oauth2_scheme)], request: Request, db: Session = Depends(get_db)):
    if not token: 
        token = request.cookies.get("access_token")
    try:
        return decode_jwt(token, db)
    except Exception as ex:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        raise credentials_exception

class PermissionChecker:
    def __init__(self, permissions_required: List[str]):
        self.permissions_required = permissions_required

    def __call__(self, token_data: TokenData = Depends(depend_token)):
        for permission_required in self.permissions_required:
            if permission_required not in [k for k, v in token_data.permissions.items() if v == True]:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Not enough permissions to access this resource")
        return token_data  

@router.post("/login", response_model=LoginToken)
def authenticate_for_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    user = authenticate(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if get_user_status(form_data.username, db) == "Inactive":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Account inactive, please reset your password",
            headers={"WWW-Authenticate": "Bearer"},
        ) 
    access_token_expires = timedelta(minutes=30)
    user_permissions = get_userpermission(user.id, db)
    access_token = generate_jwt(
        data={"sub": str(user.id), "email": user.email, "permissions": user_permissions}, expires_delta=access_token_expires
    )
    # set access token to response cookie
    response = responses.JSONResponse(jsonable_encoder({"access_token": access_token, "token_type": "bearer", **jsonable_encoder(user), **user_permissions})) # outsmart swagger.io
    response.set_cookie(key="access_token", value=f"{access_token}", httponly=True)
    return response


"""Endpoint to request a password reset via email

Parameters:
    email (str): Email address which shall have a password reset 
    request (Request): [Description]

Returns:
    HTTP: 202 Accepted in every case
"""
@router.post("/forgot-password", status_code=status.HTTP_202_ACCEPTED)
def forgot_password(email: str, request: Request, db: Session = Depends(get_db)):
    user = get_user_by_email(email, db)
    if user:
        user_to_change = ShowUser (
            id = user.id,
            email = user.email,
            status = user.status
            )
        expiration_time = timedelta(days=2)
        reset_token = generate_jwt({"sub": str(user_to_change.id),"email": user_to_change.email}, expires_delta=expiration_time)

        token_to_change = UpdateToken (
            userId = user_to_change.id,
            registrationToken = reset_token,
            registrationTokenValidUntil = datetime.now() + expiration_time
        )
        updated_token = update_token(token_to_change, db)
    #TODO: change dev env for server
        if updated_token:
            return sendEmail(template="sample",to=user_to_change.email, subj="Passwort zurücksetzen", replyTo="noreply@test.com",
                  fields={"name":user.firstname,
                          "message":f"//nIt looks like your forgot your password. Please reset your password here: //n{request.base_url}reset-password/{updated_token.registrationToken}"})
        else:
            return
    else:
        return


"""Endpoint that handles password reset given a token

Parameters:
    reset_token: JWT from url param

Returns:
    HTTP: 202 Accepted or 401 Unauthorized if token validation fails
"""
@router.post("/reset-password/{reset_token}", status_code=status.HTTP_202_ACCEPTED)
def reset_password(reset_user: ResetUser, reset_token, db: Session = Depends(get_db)): 
    try:
        token_data = decode_jwt(reset_token, db)
    except:
         raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token is expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    reset_req = get_reset_token(reset_token, db)
    if reset_req and reset_req.registrationTokenValidUntil.timestamp() > datetime.now().timestamp() and reset_req.registrationToken == reset_token: #validate token against database, even if jwt is valid
        secret_to_change = UserSecret (
            userId = token_data.userId,
            password = get_hash(reset_user.password),
            registrationToken = get_hash(create_random_secret()), #as token is already checked, token gets purged from database and replaced by a random hash
            registrationTokenValidUntil = datetime.now() - timedelta(days=1)
            )
        return update_user_secret(secret_to_change, db) 
    else: 
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token is invalid",
            headers={"WWW-Authenticate": "Bearer"},
        )
