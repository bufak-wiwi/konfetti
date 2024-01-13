from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List
from fastapi.encoders import jsonable_encoder

from db.session import get_db
from db.models.conference import Conference
from db.models.applicationType import ApplicationType
from db.models.conferenceApplication import ConferenceApplication
from db.models.report import Report


def get_application(userId: int,conferenceId:int, db: Session = Depends(get_db)):
     
    q = db.query(ApplicationType.name,ConferenceApplication.status,ConferenceApplication.isAllowedToVote,ConferenceApplication.priority,ApplicationType.goIsAllowed).join(ApplicationType,ConferenceApplication.applicationTypeId == ApplicationType.id).filter(ConferenceApplication.userId == userId, ConferenceApplication.conferenceId == conferenceId)
    return jsonable_encoder(db.execute(q).mappings().first())