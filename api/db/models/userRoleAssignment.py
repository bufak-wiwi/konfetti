from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class UserRoleAssignment(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('user.id'), nullable=False, primary_key=True)
    roleId = Column(Integer, ForeignKey('role.id'), nullable=False, primary_key=True)
    conferenceId = Column(Integer, ForeignKey('conference.id'))
                                              
    user = relationship("user", backref="conferenceApplication")
    conference = relationship("conference", backref="conferenceApplication")
    role = relationship("role", backref="conferenceApplication")