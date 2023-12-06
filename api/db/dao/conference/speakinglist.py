import datetime
import json
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
from fastapi.encoders import jsonable_encoder


# def get_speaking_list(db: Session = Depends(get_db)):
#     return db.query(Report).filter(Report.reportStatus == 0, Report.reportType == 1).order_by(Report.reportTime).all()

def get_speaking_list(db: Session):
    try:
        query= db.query(User.firstname, User.lastname, Council.university, Report.reportType, Report.reportTime, User.id, Report.reportApplicationInfo).join(Report, Report.userId == User.id).join(Council, User.councilId == Council.id).filter(Report.reportStatus == 1).order_by(asc(Report.reportTime)); 
        return jsonable_encoder(db.execute(query).mappings().all())
    except Exception as e:
        print(f"Error: {e}")
    # query.join(Report, Report.userId == User.id);
    # query.join(Council, User.councilId == Council.id);
    # query.filter(Report.reportStatus == 0);
    # query.order_by(asc(Report.reportTime));
    # return query 

def post_entry_to_speaking_list(userId:int, reportType:int,  db: Session):
    pass

def update_entry_in_speaking_list( userId:int, reportType:int, db: Session):
    pass

# Custom encoder function to handle datetime objects
def custom_encoder(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()  # Convert datetime to ISO 8601 format
    else:
        return obj