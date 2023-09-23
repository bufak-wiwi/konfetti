from sqlalchemy import Column, Integer, String, DateTime, JSON

class Conference(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    startDate = Column(DateTime, nullable=False)
    endDate = Column(DateTime, nullable=False)
    participationAgreement = Column(String(255), nullable=False)
    arrivedCouncils = Column(Integer, nullable=False)
    conferenceApplicationPhase = Column(JSON, nullable=False)
    workshopApplicationPhase = Column(JSON, nullable=False)
    workshopSuggestionPhase = Column(JSON, nullable=False)
    texte = Column(JSON, nullable=False)
    dropdowns = Column(JSON, nullable=False)