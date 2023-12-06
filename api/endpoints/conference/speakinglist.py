import json
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, responses

from db.dao.user import get_users
from db.dao.conference.conference import get_application
from db.dao.conference.speakinglist import get_speaking_list,post_entry_to_speaking_list, update_entry_in_speaking_list
from endpoints.auth import PermissionChecker, depend_token
from endpoints.helper.auth.authHelper import refresh_token_in_response
from endpoints.schemas.auth import TokenData
from endpoints.schemas.conference.speakinglist import SpeakingListAdd,SpeakingListUpdate,SpeakingListEntry
from endpoints.errorhandler import errorhandler
from db.session import get_db
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter()

# to refresh the token set the Response to
# response.set_cookie(key="access_token", value=f"Bearer {refresh_access_token()}", httponly=True)


"""Endpoint to get all queued speaker

Returns:
    HTTP: 202
"""
@router.get("/", dependencies=[Depends(PermissionChecker(["USER"]))],response_model=List[SpeakingListEntry])
def get_all(conferenceId:int,db: Session = Depends(get_db),current_user: TokenData = Depends(depend_token)):
    try:
        return refresh_token_in_response(JSONResponse(jsonable_encoder(get_speaking_list(db))), current_user)
    except Exception as ex:
        errorhandler(ex)
    
# @router.get("/{conferenceId}/important", dependencies=[Depends(PermissionChecker(["USER"]))])
# def get_all(conferenceId:int):
#     try:
#         speaking_list = get_speaking_list_important()
#         response = responses.Response(speaking_list)
#         return refresh_token_in_response(response)
#     except Exception as ex:
#         errorhandler(ex)
    
@router.post("/raiseHand", status_code=status.HTTP_201_CREATED,dependencies=[Depends(PermissionChecker(["USER"]))])
def add_Report(conferenceId:int,body:SpeakingListAdd, current_user: TokenData = Depends(depend_token)):
    try:
        applicationInfo = get_application(current_user.userId,conferenceId)
        print(applicationInfo)
        post_entry_to_speaking_list(current_user.userId,body.reportType,applicationInfo.applicationType)
        pass
    except Exception as ex:
        errorhandler(ex)

@router.post("/lowerHand", status_code=status.HTTP_201_CREATED,dependencies=[Depends(PermissionChecker(["USER"]))])
def update_Report(conferenceId:int,body:SpeakingListUpdate, current_user: TokenData = Depends(depend_token)):
    try:
        update_entry_in_speaking_list(body.reportId, current_user.userId)
        pass
    except Exception as ex:
        errorhandler(ex)

@router.post("/lowerHand/admin", status_code=status.HTTP_201_CREATED,dependencies=[Depends(PermissionChecker(["ADMIN"]))])
def update_Report(conferenceId:int,body:SpeakingListUpdate):
    try:
        update_entry_in_speaking_list(body.reportId, body.userId)
        pass
    except Exception as ex:
        errorhandler(ex)
