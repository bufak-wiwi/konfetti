"""
New API for conferencemanagementsystem for BuFaK


@2run: uvicorn main:app --reload
@version: v0.9, 22.09.2023
@author: DHR
"""
import os
from dotenv import load_dotenv

from fastapi import FastAPI, Request

from db.session import engine 
from db.base import Base
from endpoints.api import api_router
from endpoints.auth import PermissionChecker, get_current_user, refresh_access_token

load_dotenv()

"""Basic create of all Databasetables if not existing by sqlalchemy

"""
def create_tables():         
	Base.metadata.create_all(bind=engine)
        
"""basic startup of the server app and router

Returns:
    FastAPI approuter
"""
def start_application():
    app = FastAPI(title=os.getenv("APP_NAME"),version=os.getenv("APP_VERSION"))
    create_tables()
    app.include_router(api_router, prefix="/api")
    return app


app = start_application()

"""Request/Reponse middleware

Returns:
    HTTP: Response calculated by the path-endpointfunction
"""
# @app.middleware("http")
# async def add_access_token(request: Request, call_next):
#     # do something with the request before passing to endpointfunction
#     # token = request.cookies.get("access_token")

#     # pass the request to the endpointfunction, automatic identified by the path
#     response = await call_next(request)

#     # # do something with the response before returning
#     # if token:
#     #     response.set_cookie(key="access_token", value=f"{refresh_access_token(current_user = get_current_user(token))}", httponly=True)

#     return response


"""Endpointfunction on the root of the api, basic return to test the serverstartup

Returns:
    HTTP: Hello World!
"""
@app.get("/")
async def root():
    return {"message": f"Hello World! We are here :), The Application is up and running in current version: {os.getenv('APP_VERSION')}"}
