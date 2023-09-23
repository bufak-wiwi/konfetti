from sqlalchemy import Column, Integer, String, Boolean
from db.models.base import Base


class ApplicationCode(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    conferenceid = Column(Integer, nullable=False)
    councilId = Column(Integer, nullable=False)
    priority = Column(Integer, nullable=False)
    code = Column(String(255), nullable=False)
    isUsed = Column(Boolean, nullable=False)
    typeId = Column(Integer, nullable=False)