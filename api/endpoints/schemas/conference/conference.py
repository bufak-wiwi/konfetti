from pydantic import BaseModel
from datetime import datetime

# Representationschema for the requestbody to create a user
class UserDetails(BaseModel):
    reportType: int

# # Representationschema for the requestbody to update a user
# class SpeakingListUpdate(BaseModel):
#     reportId: int
#     userId: int
# class SpeakingListEntry(BaseModel):
#     name:str
#     surname:str
#     council:str
#     reportType:int
#     reportTime:str
#     reportApplicantInfo:str

class NewConferenceDetails(BaseModel):
    name: str
    startDate: datetime
    endDate: datetime
    participationAgreement: str
    arrivedCouncils: int
    conferenceApplicationPhase: str
    workshopApplicationPhase: str
    workshopSuggestionPhase: str
    texts: str
    dropdowns: str
    hostId: int

class ConferenceDetails(BaseModel):
    id: int
    name: str
    startDate: datetime
    endDate: datetime
    participationAgreement: str
    arrivedCouncils: int
    conferenceApplicationPhase: str
    workshopApplicationPhase: str
    workshopSuggestionPhase: str
    texts: str
    dropdowns: str

    class Config:  # tells pydantic to convert even non dict obj to json
        orm_mode = True

