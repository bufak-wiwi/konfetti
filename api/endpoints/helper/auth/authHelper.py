import os
import string, random
from dotenv import load_dotenv
from datetime import datetime, timedelta
from typing import Annotated, List

from fastapi import Depends, Request, HTTPException, status
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from endpoints.schemas.auth import TokenData
from db.dao.user import get_user, get_reset_token
from db.models.user import User

load_dotenv()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/login")

def generate_jwt(data: dict, type: str = "access", expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire, "type": type})
    encoded_jwt = jwt.encode(to_encode, os.getenv("JWT_SECRET"), algorithm="HS256")
    return encoded_jwt


def decode_jwt(token, db: Session):
    payload = jwt.decode(token, os.getenv("JWT_SECRET"), algorithms=["HS256"])
    userId: str = payload.get("sub")
    if "permissions" in payload.keys():
        user_permissions: dict = payload.get("permissions")
    else: 
        user_permissions: dict = {}
    if "email" in payload.keys():
        user_email: str = payload.get("email")
    else:
        user_email: str = ""
    if userId is None:
        raise JWTError
    token_data = TokenData(userId=userId, email=user_email, permissions=user_permissions)
    user: User = get_user(userId=int(token_data.userId), db=db)
    if (user is None) or (user.status == "BLOCKED"):
        raise ValueError
    return token_data

def refresh_token(encoded_jwt: TokenData, expires_delta: timedelta | None = None):
    token_data = encoded_jwt
    to_encode = dict(token_data.model_copy())
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv("JWT_SECRET"), algorithm="HS256")
    return encoded_jwt
    
def refresh_token_in_response(response, current_user):

    response.set_cookie(key="access_token", value=f"{refresh_token(encoded_jwt = current_user)}", httponly=True)

    return response

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_hash(password):
    return pwd_context.hash(password)

def create_random_secret():
    letters = list(string.ascii_letters)
    return "".join(random.choices(letters, k=48))