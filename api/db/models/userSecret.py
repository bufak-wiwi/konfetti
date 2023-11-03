from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from db.base import Base
from sqlalchemy.orm import relationship

class UserSecret(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('user.id'), nullable=False)
    password = Column(String(255), nullable=False)
    registrationToken = Column(String(255), nullable=True)
    registrationTokenValidUntil = Column(DateTime, nullable=True)
    passwordToken = Column(String(255), nullable=True)
    passwordTokenValidUntil = Column(DateTime, nullable=True)

    user = relationship("User", backref="userSecret")
