from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, responses

from db.dao.user import get_users
from db.dao.conference.conference import get_application
from db.dao.conference.speakinglist import get_speaking_list,post_entry_to_speaking_list, get_speaking_list_important, update_entry_in_speaking_list
from endpoints.auth import PermissionChecker, get_current_user, refresh_access_token
from endpoints.schemas.auth import TokenData
from endpoints.schemas.user import ShowUser, CreateUser, UpdateUser
from endpoints.errorhandler import errorhandler

router = APIRouter()

class SpeakingListAdd:
    def __init__(self, conferenceId: int, reportType: int):
        self.conferenceId = conferenceId
        self.reportType = reportType

class SpeakingListUpdate:
    def __init__(self, reportId: int, userId):
        self.reportId = reportId
        self.userId = userId

# to refresh the token set the Response to
# response.set_cookie(key="access_token", value=f"Bearer {refresh_access_token()}", httponly=True)

@router.get("/", dependencies=[Depends(PermissionChecker(["USER"]))], response_model=List[ShowUser])
def get_all():
    try:
        speaking_list = get_speaking_list
        response = responses.Response(speaking_list)
        response.set_cookie(key="access_token", value=f"Bearer {refresh_access_token()}", httponly=True)
        return response
    except Exception as ex:
        errorhandler(ex)
    
@router.get("/important", dependencies=[Depends(PermissionChecker(["USER"]))], response_model=List[ShowUser])
def get_all():
    try:
        speaking_list = get_speaking_list_important()
        response = responses.Response(speaking_list)
        response.set_cookie(key="access_token", value=f"Bearer {refresh_access_token()}", httponly=True)
        return response
    except Exception as ex:
        errorhandler(ex)
    
@router.post("/raiseHand", status_code=status.HTTP_201_CREATED,dependencies=[Depends(PermissionChecker(["USER"]))], response_model=List[ShowUser])
def add_Report(body:SpeakingListAdd, current_user: TokenData = Depends(get_current_user)):
    try:
        applicationInfo = get_application(current_user.userId,body.conferenceId)
        post_entry_to_speaking_list(current_user.userId,body.reportType,applicationInfo.applicationType)
    except Exception as ex:
        errorhandler(ex)
@router.post("/lowerHand", status_code=status.HTTP_201_CREATED,dependencies=[Depends(PermissionChecker(["USER"]))], response_model=List[ShowUser])
def update_Report(body:SpeakingListUpdate, current_user: TokenData = Depends(get_current_user)):
    try:
        update_entry_in_speaking_list(body.reportId, current_user.userId)
    except Exception as ex:
        errorhandler(ex)
@router.post("/lowerHand/admin", status_code=status.HTTP_201_CREATED,dependencies=[Depends(PermissionChecker(["ADMIN"]))], response_model=List[ShowUser])
def update_Report(body:SpeakingListUpdate):
    try:
        update_entry_in_speaking_list(body.reportId, body.userId)
    except Exception as ex:
        errorhandler(ex)
