from sqlalchemy import Column, Integer, String, DateTime

class Travel(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    conferenceId = Column(Integer, nullable=False)
    userId = Column(Integer, nullable=False)
    transportation = Column(String(255), nullable=False)
    parkingspace = Column(Integer, nullable=False)
    arrivalTimestamp = Column(DateTime, nullable=False)
    arrivalPlace = Column(String(255), nullable=False)
    departureTimestamp = Column(DateTime, nullable=False)
    note = Column(String(255), nullable=False)