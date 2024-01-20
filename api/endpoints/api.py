from fastapi import APIRouter

from endpoints import auth
from endpoints import user
from endpoints.conference import speakinglist
from endpoints.conference import conference
#from endpoints.conferences import conferences

api_router = APIRouter()

# map all endpoints to routeprefixes
api_router.include_router(auth.router, prefix="", tags=["auth"])
api_router.include_router(user.router, prefix="/users", tags=["users"])
#api_router.include_router(conferences.router, prefix="/conference/", tags=["conferences"])
api_router.include_router(conference.router, prefix="", tags=["conference"]) #changed prefic from /conference/{id} because of different handling in endpoint
api_router.include_router(speakinglist.router, prefix="/conference/{conferenceId}/speakinglist", tags=["speakinglist"])