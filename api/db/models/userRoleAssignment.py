from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base
class UserRoleAssignment(Base):
    userId = Column(Integer, ForeignKey('user.id'), nullable=False)
    roleId = Column(Integer, ForeignKey('role.id'), nullable=False)
    conferenceId = Column(Integer, ForeignKey('conference.id'), nullable=False, primary_key=True)
                                              
user = relationship("user", backref="conferenceApplication")
conference = relationship("conference", backref="conferenceApplication")
role = relationship("role", backref="conferenceApplication")