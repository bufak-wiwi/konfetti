"""
New API for conferencemanagementsystem for BuFaK


@2run: uvicorn main:app --reload
@version: v0.9, 22.09.2023
@author: DHR
"""
import os
from dotenv import load_dotenv
from pathlib import Path

from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

# dev temp
from typing import Annotated
from fastapi import Depends

from db.session import engine 
from db.models.base import Base
from endpoints.api import api_router
from db.dao.user import get_current_user

load_dotenv()

def create_tables():         
	Base.metadata.create_all(bind=engine)
        

def start_application():
    app = FastAPI(title=os.getenv("APP_NAME"),version=os.getenv("APP_VERSION"))
    create_tables()
    app.include_router(api_router, prefix="/api")
    return app


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
app = start_application()


@app.get("/")
async def root():
    return {"message": f"Hello World!, The Application is up and running in current version: {os.getenv('APP_VERSION')}"}

# dev temp
@app.get("/secure")
async def secret(current_user: Annotated[str, Depends(get_current_user)]):
    return {"message": "Hello secret World!", "current User": current_user}