from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from db.base import Base
from sqlalchemy.orm import relationship

class ApplicationCode(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    conferenceId = Column(Integer, ForeignKey('conference.id'), nullable=False)
    councilId = Column(Integer, ForeignKey('council.id'), nullable=False)
    priority = Column(Integer, nullable=False)
    code = Column(String(255), nullable=False)
    isUsed = Column(Boolean, nullable=False)
    applicationTypeId = Column(Integer, ForeignKey('applicationtype.id'), nullable=False)

    conference = relationship("conference", backref="applicationCode")
    council = relationship("council", backref="applicationCode")
    applicationType = relationship("applicationType", backref="applicationCode")