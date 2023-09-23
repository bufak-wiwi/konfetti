from sqlalchemy import String, Integer, Column, JSON
from sqlalchemy import Base

class ApplicationType(Base):
    id = Column(Integer, autoincrement=True, primary_key=True)
    sex = Column(String(255), nullable=False)
    street = Column(String(255), nullable=False)
    zip = Column(Integer, nullable=False)
    city = Column(String(255), nullable=False)
    comment = Column(String(255), nullable=False)
    sleepingPreference = Column(String(255), nullable=False)
    eatingPreference = Column(String(255), nullable=False)
    intolerances = Column(String(255), nullable=False)
    phone = Column(String(255), nullable=False)
    conferenceCount = Column(Integer, nullable=False)
    accomodation = Column(JSON, nullable=False)