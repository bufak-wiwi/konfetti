from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class ApiKey(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    apiKey = Column(String(255), nullable=False)
    note = Column(String(255), nullable=False)
    createdOn = Column(Date, nullable=False)
    validUntil = Column(Date, nullable=True)
    conferenceId = Column(Integer, ForeignKey('conference.id'), nullable=False)


    conference = relationship("conference", backref="apiKey")
 