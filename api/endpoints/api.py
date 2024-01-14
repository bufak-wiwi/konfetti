from fastapi import APIRouter

from endpoints import auth, user, votingAnswer, votingQuestion

api_router = APIRouter()

# map all endpoints to routeprefixes
api_router.include_router(auth.router, prefix="", tags=["auth"])
api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(votingQuestion.router, prefix="/votingQuestions", tags=["voting"])
api_router.include_router(votingAnswer.router, prefix="/votingAnswers", tags=["voting"])