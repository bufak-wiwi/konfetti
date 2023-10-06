from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List

from db.session import get_db
from db.models.conference import Conference
from db.models.conferenceApplication import ConferenceApplication
from db.models.report import Report



def get_speaking_list(db: Session = Depends(get_db)):
    return db.query(Report).filter(Report.reportStatus == 0, Report.reportType == 1).order_by(Report.reportTime).all()

def get_speaking_list_important(db: Session = Depends(get_db)):
    return db.query(Report).filter(Report.reportStatus == 0, Report.reportType == 0).order_by(Report.reportTime).all()

def post_entry_to_speaking_list(userId:int, reportType:int, applicationInfo:str, db: Session = Depends(get_db)):
    pass

def update_entry_in_speaking_list(reportId:int, userId:int, db: Session = Depends(get_db)):
    pass