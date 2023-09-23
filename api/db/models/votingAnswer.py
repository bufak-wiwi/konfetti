from sqlalchemy import Column, Integer, String, ForeignKey
from db.base import Base
from sqlalchemy.orm import relationship

class VotingAnswer(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    questionId = Column(Integer, ForeignKey('votingquestion.id'),  nullable=False)
    councilId = Column(Integer, ForeignKey('council.id'), nullable=False)
    priority = Column(Integer, nullable=False)
    vote = Column(String(255), nullable=False)

    council = relationship("council", backref="votingAnswer")
    votingQuestion = relationship("votingQuestion", backref="votingAnswer")