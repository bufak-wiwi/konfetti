"""
New API for conferencemanagementsystem for BuFaK


@2run: uvicorn main:app --reload
@version: v0.9, 22.09.2023
@author: DHR
"""
import os
from dotenv import load_dotenv

from fastapi import FastAPI

from db.session import engine 
from db.base import Base
from endpoints.api import api_router

load_dotenv()

def create_tables():         
	Base.metadata.create_all(bind=engine)
        

def start_application():
    app = FastAPI(title=os.getenv("APP_NAME"),version=os.getenv("APP_VERSION"))
    create_tables()
    app.include_router(api_router, prefix="/api")
    return app


app = start_application()


@app.get("/")
async def root():
    return {"message": f"Hello World!, The Application is up and running in current version: {os.getenv('APP_VERSION')}"}
