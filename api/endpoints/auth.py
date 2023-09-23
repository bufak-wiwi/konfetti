import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from typing import Annotated, List
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext


from db.dao.user import get_user, get_user_for_login, get_userpermission
from db.models.user import User
from endpoints.schemas.auth import TokenData

load_dotenv()

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_hash(password):
    return pwd_context.hash(password)

def authenticate(username: str, password: str):
    user = get_user_for_login(username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv("PWD_SECRET"), algorithm="HS256")
    return encoded_jwt


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, os.getenv("PWD_SECRET"), algorithms=["HS256"])
        userId: str = payload.get("sub")
        user_permissions: dict = payload.get("permissions")
        if userId is None:
            raise credentials_exception
        token_data = TokenData(userId=userId, permissions=user_permissions)
    except JWTError:
        raise credentials_exception
    user: User = get_user(id=token_data.userId)
    if (user is None) or (user.status == "BLOCKED"):
        raise credentials_exception
    return token_data

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


@router.post("/login")
def authenticate_for_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.id, "permissions": get_userpermission(user.id)}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

