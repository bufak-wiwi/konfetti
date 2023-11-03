import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from typing import Annotated, List
from fastapi import Depends, APIRouter, HTTPException, Request, status, responses
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from db.session import get_db
from db.dao.user import get_user, get_user_for_login, get_userpermission, get_user_status, send_reset, update_user_secret
from db.models.user import User
from endpoints.schemas.user import ShowUser, UpdateUser
from endpoints.schemas.auth import TokenData, LoginToken

load_dotenv()

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/login")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_hash(password):
    return pwd_context.hash(password)

def authenticate(username: str, password: str, db: Session):
    user_secrect = get_user_for_login(username, db = db)
    if not user_secrect:
        return False
    if not verify_password(password, user_secrect.password):
        return False
    return get_user(user_secrect.userId, db)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv("JWT_SECRET"), algorithm="HS256")
    return encoded_jwt


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], request: Request, db: Session = Depends(get_db)):
    if not token: 
        token = request.cookies.get("access_token")
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, os.getenv("JWT_SECRET"), algorithms=["HS256"])
        userId: str = payload.get("sub")
        user_permissions: dict = payload.get("permissions")
        user_email: str = payload.get("email")
        if userId is None:
            raise credentials_exception
        token_data = TokenData(userId=userId, email=user_email, permissions=user_permissions)
    except JWTError:
        raise credentials_exception
    user: User = get_user(userId=int(token_data.userId), db=db)
    if (user is None) or (user.status == "BLOCKED"):
        raise credentials_exception
    return token_data

def refresh_access_token(current_user: TokenData = Depends(get_current_user), expires_delta: timedelta | None = None):
    token_data = current_user
    to_encode = dict(token_data.model_copy())
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv("JWT_SECRET"), algorithm="HS256")
    return encoded_jwt

class PermissionChecker:
    def __init__(self, permissions_required: List[str]):
        self.permissions_required = permissions_required

    def __call__(self, token_data: TokenData = Depends(get_current_user)):
        for permission_required in self.permissions_required:
            if permission_required not in [k for k, v in token_data.permissions.items() if v == True]:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Not enough permissions to access this resource")
        return token_data
    

def refresh_token_in_response(response, current_user):

    response.set_cookie(key="access_token", value=f"{refresh_access_token(current_user = current_user)}", httponly=True)

    return response


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
    access_token = create_access_token(
        data={"sub": str(user.id), "email": user.email, "permissions": user_permissions}, expires_delta=access_token_expires
    )
    # set access token to response cookie
    response = responses.JSONResponse(jsonable_encoder({"access_token": access_token, "token_type": "bearer", **jsonable_encoder(user), **user_permissions})) # outsmart swagger.io
    response.set_cookie(key="access_token", value=f"{access_token}", httponly=True)
    return response


    #TODO: forgot pw functionality and proper email handling
@router.post("/forgot-password", status_code=status.HTTP_202_ACCEPTED)
def forgot_password(email: str, db: Session = Depends(get_db)):
    #return send_reset(email, db)
    pass
    
    #TODO: reset pw functionality with token handling
@router.post("/reset-password")
def reset_password(db: Session = Depends(get_db)):
    # reset token validation
    # pw hash
    # send pw hash and new token to update_user_secret() in user dao
    pass