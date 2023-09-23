from sqlalchemy import Column, Integer, String, DateTime

class UserSecret(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, nullable=False)
    password = Column(String(255), nullable=False)
    registrationToken = Column(String(255), nullable=False)
    registrationTokenValidUntil = Column(DateTime, nullable=False)
    passwordToken = Column(String(255), nullable=False)
    passwordTokenValidUntil = Column(DateTime, nullable=False)
