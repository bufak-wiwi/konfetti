from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

"""
Api key for custom applications (e.g. third party apps).
Using this key in the x-api-key header will allow the user to access all endpoints as he would be logged in.
"""
class ApiKey(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    """"hash of the api key"""
    apiKey = Column(String(255), nullable=False)
    note = Column(String(255), nullable=False)
    createdOn = Column(Date, nullable=False)
    validUntil = Column(Date, nullable=True)
    userId = Column(Integer, ForeignKey('user.id'), nullable=False)


    user = relationship("user", backref="apiKey")
 