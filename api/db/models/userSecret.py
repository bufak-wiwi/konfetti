from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from db.models.base import Base
from sqlalchemy.orm import relationship

class UserSecret(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('user.id'), nullable=False)
    password = Column(String(255), nullable=False)
    registrationToken = Column(String(255), nullable=False)
    registrationTokenValidUntil = Column(DateTime, nullable=False)
    passwordToken = Column(String(255), nullable=False)
    passwordTokenValidUntil = Column(DateTime, nullable=False)

user = relationship("user", backref="userSecret")