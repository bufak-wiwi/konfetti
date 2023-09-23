from sqlalchemy import Column, Integer, Boolean
from db.models.base import Base

class WorkshopApplication(Base):
    workshopId = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, primary_key=True)
    priority = Column(Integer, nullable=False)
    isHost = Column(Boolean, nullable=False)