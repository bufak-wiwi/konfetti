from sqlalchemy import Column, Integer, Boolean, ForeignKey
from db.models.base import Base
from sqlalchemy.orm import relationship

class WorkshopApplication(Base):
    workshopId = Column(Integer, ForeignKey('workshop.id'), primary_key=True,  autoincrement=True)
    userId = Column(Integer, ForeignKey('user.id'), primary_key=True)
    priority = Column(Integer, nullable=False)
    isHost = Column(Boolean, nullable=False)

    user = relationship("user", backref="workshopApplication")
    workshop = relationship("workshop", backref="workshopApplication")