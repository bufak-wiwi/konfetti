from sqlalchemy import Column, Integer, String, Boolean
from db.models.base import Base

class Council(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    zip = Column(Integer, nullable=False)
    city = Column(String(255), nullable=False)
    university = Column(String(255), nullable=False)
    street = Column(String(255), nullable=False)
    isBlocked = Column(Boolean, nullable=False)