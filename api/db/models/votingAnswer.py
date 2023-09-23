from sqlalchemy import Column, Integer, String
from db.models.base import Base

class VotingAnswer(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    questionId = Column(Integer, nullable=False)
    councilId = Column(Integer, nullable=False)
    priority = Column(Integer, nullable=False)
    vote = Column(String(255), nullable=False)
