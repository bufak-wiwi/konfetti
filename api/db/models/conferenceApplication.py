from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class ConferenceApplication(Base):
    userId = Column(Integer, ForeignKey('user.id'), nullable=False, primary_key=True)
    conferenceId = Column(Integer, ForeignKey('conference.id'), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    priority = Column(Integer, nullable=False)
    sensibleId = Column(Integer, ForeignKey('sensible.id'), nullable=True)
    councilId = Column(Integer, ForeignKey('council.id'), nullable=False)
    status = Column(String(255), nullable=False)
    isAllowedToVote = Column(Boolean, nullable=False)
    applicationTypeId = Column(Integer, ForeignKey('applicationtype.id'), nullable=False)

    user = relationship("User", backref="ConferenceApplication")
    conference = relationship("Conference", backref="ConferenceApplication")
    sensible = relationship("Sensible", cascade='delete', backref="ConferenceApplication")
    council = relationship("Council", backref="ConferenceApplication")
    applicationType = relationship("ApplicationType", backref="ConferenceApplication")  