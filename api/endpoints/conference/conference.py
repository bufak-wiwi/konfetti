import json
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, responses

from db.dao.user import get_users
from db.dao.conference.conference import get_application, create_conference_in_db, update_conference_in_db, get_conference_by_id, get_council_list, set_host_council
from db.dao.conference.speakinglist import get_speaking_list,post_entry_to_speaking_list,check_if_report_exists, update_entry_in_speaking_list
from endpoints.auth import PermissionChecker, depend_token
from endpoints.helper.auth.authHelper import refresh_token_in_response
from endpoints.schemas.auth import TokenData
from endpoints.schemas.conference.speakinglist import SpeakingListAdd,SpeakingListUpdate,SpeakingListEntry
from endpoints.schemas.conference.conference import UserDetails, NewConferenceDetails, ConferenceDetails
from endpoints.schemas.council import Council

from endpoints.errorhandler import errorhandler
from db.session import get_db
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter()

# to refresh the token set the Response to
# response.set_cookie(key="access_token", value=f"Bearer {refresh_access_token()}", httponly=True)


@router.get("/getApplicationDetails", dependencies=[Depends(PermissionChecker(["USER"]))], response_model=List[UserDetails])
def get_user_details(conferenceId:int,db: Session = Depends(get_db), current_user: TokenData = Depends(depend_token)):
    try:
        applicationInfo = get_application(current_user.userId,conferenceId,db)
        print(applicationInfo)
        return refresh_token_in_response(JSONResponse(applicationInfo),current_user)
    except Exception as ex:
        errorhandler(ex)


#TODO: get working
@router.get("/conferenceDetails/{conferenceId}")
def get_conference_details(conferenceId: int, db: Session = Depends(get_db)):
    return get_conference_by_id(conferenceId, db)

#TODO:get working
@router.get("/newConference", dependencies=[Depends(PermissionChecker(["ADMIN"]))])
def get_councils(db: Session = Depends(get_db)):
    return get_council_list(db)

@router.post("/newConference/create", dependencies=[Depends(PermissionChecker(["ADMIN"]))], status_code=status.HTTP_201_CREATED)
def create_new_conference(conference2create: NewConferenceDetails, db: Session = Depends(get_db), current_user: TokenData = Depends(depend_token)):
    try:
        newConference = create_conference_in_db(conference2create, db)
        if newConference:
            hostRole = set_host_council(newConference.id, NewConferenceDetails.hostId) #TODO: figure out how to assign host roles
        return newConference
    except Exception as ex:
        errorhandler(ex) 

#TODO: check response model functionality
@router.put("/updateConference", dependencies=[Depends(PermissionChecker(["HOST" or "ADMIN"]))], response_model=List[ConferenceDetails]) 
def update_conference(conference2update: ConferenceDetails, db: Session = Depends(get_db), current_user: TokenData = Depends(depend_token)):
    try:
        updatedConference = update_conference_in_db(conference2update, db)
        return updatedConference
    except Exception as ex:
        errorhandler(ex)

#TODO: figure out how to make it for all
@router.get("/getCSV/{table}", dependencies=[Depends(PermissionChecker(["HOST" or "ADMIN"]))])
def create_csv(table: str):

    pass