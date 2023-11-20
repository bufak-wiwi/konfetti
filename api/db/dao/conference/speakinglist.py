from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import and_, desc, asc
from db.session import get_db
from db.models.conference import Conference
from db.models.conferenceApplication import ConferenceApplication
from db.models.report import Report
from db.models.user import User
from db.models.conference import Conference
from db.models.council import Council


def get_speaking_list(db: Session = Depends(get_db)):
    return db.query(Report).filter(Report.reportStatus == 0, Report.reportType == 1).order_by(Report.reportTime).all()

def get_speaking_list_important(db: Session = Depends(get_db)):
    query = db.query(User.Name, User.Surname, Council.University, Report.ReportType, Report.ReportTime, User.UID, Report.ReportApplicantInfo); 
    db.join(Report, Report.UserID == User.UID);
    db.join(Council, User.CouncilID == Council.CouncilID);
    db.filter(Report.ReportStatus == 0);
    db.order_by(asc(Report.ReportTime));
    return query 

def post_entry_to_speaking_list(userId:int, reportType:int,  db: Session = Depends(get_db)):
    pass

def update_entry_in_speaking_list( userId:int, reportType:int, db: Session = Depends(get_db)):
    pass