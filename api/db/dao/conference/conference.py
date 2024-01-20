from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List
from fastapi.encoders import jsonable_encoder

from db.session import get_db
from db.models.conference import Conference
from db.models.applicationType import ApplicationType
from db.models.conferenceApplication import ConferenceApplication
from db.models.report import Report
from db.models.council import Council


def get_application(userId: int, conferenceId: int, db: Session):
     
    q = db.query(ApplicationType.name,ConferenceApplication.status,ConferenceApplication.isAllowedToVote,ConferenceApplication.priority,ApplicationType.goIsAllowed).join(ApplicationType,ConferenceApplication.applicationTypeId == ApplicationType.id).filter(ConferenceApplication.userId == userId, ConferenceApplication.conferenceId == conferenceId)
    return jsonable_encoder(db.execute(q).mappings().first())

#TODO: test
def create_conference_in_db(newConference, db: Session):
     newConferenceEntry = Conference(
        name = newConference.name,
        startDate = newConference.startDate,
        endDate = newConference.endDate,
        participationAgreement = newConference.participationAgreement,
        arrivedCouncils = newConference.arrivedCouncils,
        conferenceApplicationPhase = newConference.conferenceApplicationPhase,
        workshopApplicationPhase = newConference.workshopApplicationPhase,
        workshopSuggestionPhase = newConference.workshopSuggestionPhase,
        texts = newConference.texts,
        dropdowns = newConference.dropdowns
     )
     db.add(newConferenceEntry)
     db.commit()
     return newConferenceEntry

#TODO: test
def update_conference_in_db(updateConference, db: Session):
    conferenceUpdate = db.query(Conference).filter(Conference.id == updateConference.id).first()

    conferenceUpdate.name = updateConference.name
    conferenceUpdate.startDate = updateConference.startDate
    conferenceUpdate.endDate = updateConference.endDate
    conferenceUpdate.participationAgreement = updateConference.participationAgreement
    conferenceUpdate.arrivedCouncils = updateConference.arrivedCouncils
    conferenceUpdate.conferenceApplicationPhase = updateConference.conferenceApplicationPhase
    conferenceUpdate.workshopApplicationPhase = updateConference.workshopApplicationPhase
    conferenceUpdate.workshopSuggestionPhase = updateConference.workshopSuggestionPhase
    conferenceUpdate.texts = updateConference.texts
    conferenceUpdate.dropdowns = updateConference.dropdowns

    db.commit()
    return
    
# TODO: test
def get_conference_by_id(conferenceId: int, db: Session):
     return db.query(Conference).filter(Conference.id == conferenceId).first()
    
#TODO: test
def get_council_list(db: Session):
     return list(db.query(Council).all())
#TODO: figure out how
def set_host_council():
     pass