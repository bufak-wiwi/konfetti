from sqlalchemy import Column, Integer, String, DateTime, Boolean

class ConferenceApplication(Base):
    userId = Column(Integer, nullable=False)
    conferenceId = Column(Integer, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    priority = Column(Integer, nullable=False)
    sensibleId = Column(Integer, nullable=False)
    councilId = Column(Integer, nullable=False)
    status = Column(String(255), nullable=False)
    isAllowedToVote = Column(Boolean, nullable=False)
    typeId = Column(Integer, nullable=False)