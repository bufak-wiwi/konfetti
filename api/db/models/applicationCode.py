from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from db.models.base import Base
from sqlalchemy.orm import relationship

class ApplicationCode(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    conferenceid = Column(Integer, ForeignKey('conference.id'), nullable=False)
    councilId = Column(Integer, ForeignKey('council.id'), nullable=False)
    priority = Column(Integer, nullable=False)
    code = Column(String(255), nullable=False)
    isUsed = Column(Boolean, nullable=False)
    typeId = Column(Integer, ForeignKey('applicationType.id'), nullable=False)

conference = relationship("conference", backref="applicationCode")
council = relationship("council", backref="applicationCode")
applicationType = relationship("applicationType", backref="applicationCode")