from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List

from db.session import get_db
from db.models.conference import Conference
from db.models.conferenceApplication import ConferenceApplication
from db.models.report import Report


def get_application(userId: int,conferenceId:int, db: Session = Depends(get_db)):
    return db.query(ConferenceApplication).filter(ConferenceApplication.userId == userId, ConferenceApplication.conferenceId == conferenceId).first()