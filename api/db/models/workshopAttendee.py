from sqlalchemy import Column, Integer, Boolean
from db.models.base import Base

class WorkshopAttendee(Base):
    workshopId = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, primary_key=True)
    isHost = Column(Boolean, nullable=False)