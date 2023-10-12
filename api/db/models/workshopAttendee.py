from sqlalchemy import Column, Integer, Boolean, ForeignKey
from db.base import Base
from sqlalchemy.orm import relationship

class WorkshopAttendee(Base):
    workshopId = Column(Integer, ForeignKey('workshop.id'), primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('user.id'), primary_key=True)
    isHost = Column(Boolean, nullable=False)

    
    user = relationship("User", backref="workshopAttendee")
    workshop = relationship("Workshop", backref="workshopAttendee")