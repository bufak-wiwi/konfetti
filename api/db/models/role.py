from sqlalchemy import Column, Integer, String

class Role(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
