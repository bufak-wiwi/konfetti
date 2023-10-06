from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db.base import Base


class Report(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('user.id'), nullable=False)
    reportType = Column(Integer, nullable=False)  #0 = GO, 1 = speakinglist
    reportStatus = Column(Integer, nullable=False) # 0 = open, 1 = done
    reportTime = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    reportApplicationInfo = Column(String(255), nullable=False)

    user = relationship("user", backref="report")