from sqlalchemy import Column, Integer, Boolean, ForeignKey
from db.models.base import Base
from sqlalchemy.orm import relationship
class WorkshopAttendee(Base):
    workshopId = Column(Integer, ForeignKey('workshop.id'), primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('user.id'), primary_key=True)
    isHost = Column(Boolean, nullable=False)

    
    user = relationship("user", backref="workshopAttendee")
    workshop = relationship("workshop", backref="workshopAttendee")