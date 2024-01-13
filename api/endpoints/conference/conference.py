import json
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, responses

from db.dao.user import get_users
from db.dao.conference.conference import get_application
from db.dao.conference.speakinglist import get_speaking_list,post_entry_to_speaking_list,check_if_report_exists, update_entry_in_speaking_list
from endpoints.auth import PermissionChecker, depend_token
from endpoints.helper.auth.authHelper import refresh_token_in_response
from endpoints.schemas.auth import TokenData
from endpoints.schemas.conference.speakinglist import SpeakingListAdd,SpeakingListUpdate,SpeakingListEntry
from endpoints.schemas.conference.conference import UserDetails
from endpoints.errorhandler import errorhandler
from db.session import get_db
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter()

# to refresh the token set the Response to
# response.set_cookie(key="access_token", value=f"Bearer {refresh_access_token()}", httponly=True)


@router.get("/getApplicationDetails", dependencies=[Depends(PermissionChecker(["USER"]))],response_model=List[UserDetails])
def get_user_details(conferenceId:int,db: Session = Depends(get_db), current_user: TokenData = Depends(depend_token)):
    try:
        applicationInfo = get_application(current_user.userId,conferenceId,db)
        print(applicationInfo)
        return refresh_token_in_response(JSONResponse(applicationInfo),current_user)
    except Exception as ex:
        errorhandler(ex)
