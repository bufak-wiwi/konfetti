from sqlalchemy import String, Integer, Column
from sqlalchemy import Base

class ApplicationType(Base):
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(255), nullable=False)