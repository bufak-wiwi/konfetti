from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class UserRoleAssignment(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('user.id'), nullable=False, index=True)
    roleId = Column(Integer, ForeignKey('role.id'), nullable=False, index=True)
    conferenceId = Column(Integer, ForeignKey('conference.id'))
                                              
    user = relationship("User", backref="userRoleAssignment")
    conference = relationship("Conference", backref="userRoleAssignment")
    role = relationship("Role", backref="userRoleAssignment")
