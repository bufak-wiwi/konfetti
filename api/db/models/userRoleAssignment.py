from sqlalchemy import Column, Integer
from db.models.base import Base

class UserRoleAssignment(Base):
    userId = Column(Integer, nullable=False)
    roleId = Column(Integer, nullable=False)
    conferenceId = Column(Integer, nullable=False, primary_key=True)
