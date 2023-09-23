from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from db.base import Base
from sqlalchemy.orm import relationship

class Travel(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    conferenceId = Column(Integer, ForeignKey('conference.id'), nullable=False)
    userId = Column(Integer, ForeignKey('user.id'), nullable=False)
    transportation = Column(String(255), nullable=False)
    parkingspace = Column(Integer, nullable=False)
    arrivalTimestamp = Column(DateTime, nullable=False)
    arrivalPlace = Column(String(255), nullable=False)
    departureTimestamp = Column(DateTime, nullable=False)
    note = Column(String(255), nullable=False)

    user = relationship("user", backref="travel")
    conference = relationship("conference", backref="travel")