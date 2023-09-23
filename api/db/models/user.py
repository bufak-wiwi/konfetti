from db.models.base import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), nullable=False, unique=True, index=True)