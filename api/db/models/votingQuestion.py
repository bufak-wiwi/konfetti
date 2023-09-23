from sqlalchemy import Column, Integer, String, Boolean, DateTime, JSON
from db.models.base import Base

class VotingQuestion(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    conferenceId = Column(Integer, nullable=False)
    type = Column(String(255), nullable=False)
    questionText = Column(String(255), nullable=False)
    arrivedCouncilCount = Column(Integer, nullable=False)
    isOpen = Column(Boolean, nullable=False)
    issecret = Column(Boolean, nullable=False)
    resolvedOn = Column(DateTime, nullable=False)
    votingOptions = Column(JSON, nullable=False)
    votes = Column(JSON, nullable=False)
    result = Column(String(255), nullable=False)
