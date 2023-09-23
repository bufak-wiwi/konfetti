from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from db.models.base import Base


class Report(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    report_type = Column(Integer, nullable=False)
    report_status = Column(Integer, nullable=False)
    report_time = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    report_application_info = Column(String(255), nullable=False)