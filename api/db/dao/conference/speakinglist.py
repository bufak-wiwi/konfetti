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


# def get_speaking_list(db: Session = Depends(get_db)):
#     return db.query(Report).filter(Report.reportStatus == 0, Report.reportType == 1).order_by(Report.reportTime).all()

def get_speaking_list(db: Session):
    t = db.query(User.firstname, User.lastname, Council.university, Report.reportType, Report.reportTime, User.id, Report.reportApplicationInfo).join(Report, Report.userId == User.id).join(Council, User.councilId == Council.id).filter(Report.reportStatus == 0).order_by(asc(Report.reportTime)); 
    return db.execute(t)
    query.join(Report, Report.userId == User.id);
    query.join(Council, User.councilId == Council.id);
    query.filter(Report.reportStatus == 0);
    query.order_by(asc(Report.reportTime));
    return query 

def post_entry_to_speaking_list(userId:int, reportType:int,  db: Session):
    pass

def update_entry_in_speaking_list( userId:int, reportType:int, db: Session):
    pass