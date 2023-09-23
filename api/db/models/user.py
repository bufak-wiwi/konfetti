from db.models.base import Base
from sqlalchemy import Column, Integer, String, Date

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), nullable=False, unique=True, index=True)
    firstname = Column(String(255), nullable=False, index=True)
    lastname = Column(String(255), nullable=False, index=True)
    councilId = Column(Integer, nullable=False, index=True)
    birthday = Column(Date, nullable=False, index=True)
    status = Column(String(255), nullable=False, index=True)