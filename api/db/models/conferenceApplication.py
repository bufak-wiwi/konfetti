from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base
class ConferenceApplication(Base):
    userId = Column(Integer, ForeignKey('user.id'), nullable=False)
    conferenceId = Column(Integer, ForeignKey('conference.id'), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    priority = Column(Integer, nullable=False)
    sensibleId = Column(Integer, ForeignKey('sensible.id'), nullable=True)
    councilId = Column(Integer, ForeignKey('council.id'), nullable=False)
    status = Column(String(255), nullable=False)
    isAllowedToVote = Column(Boolean, nullable=False)
    typeId = Column(Integer, ForeignKey('applicationType.id'), nullable=False)

    user = relationship("user", backref="conferenceApplication")
    conference = relationship("conference", backref="conferenceApplication")
    sensible = relationship("sensible", cascade='delete', backref="conferenceApplication")
    council = relationship("council", backref="conferenceApplication")
    applicationType = relationship("applicationType", backref="conferenceApplication")