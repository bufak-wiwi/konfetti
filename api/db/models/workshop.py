from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base

class Workshop(Base):

    id = Column(Integer, primary_key=True, autoincrement=True, unsigned=True)
    conferenceId = Column(Integer, ForeignKey('conference.id'), nullable=False)
    name = Column(String(255), nullable=False)
    shortname = Column(String(255), nullable=False)
    overview = Column(String(255), nullable=False)
    maxVisitors = Column(Integer, nullable=False)
    difficulty = Column(String(255), nullable=False)
    place = Column(String(255), nullable=False)
    start = Column(DateTime, nullable=False)
    duration = Column(Integer, nullable=False)
    note = Column(String(255), nullable=False)
    hostIsExternal = Column(Boolean, nullable=False)
    hostName = Column(String(255), nullable=False)

    # Define a relationship with the workshopAttendee table
    workshop_attendees = relationship("WorkshopAttendee", backref="workshop")
