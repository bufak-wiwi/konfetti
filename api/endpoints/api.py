from fastapi import APIRouter

from endpoints import auth
from endpoints import user

api_router = APIRouter()

# map all endpoints to routeprefixes
api_router.include_router(auth.router, prefix="", tags=["auth"])
api_router.include_router(user.router, prefix="/users", tags=["users"])