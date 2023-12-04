from pydantic import BaseModel

# Representationschema for the requestbody to create a user
class SpeakingListAdd(BaseModel):
    reportType: int

# Representationschema for the requestbody to update a user
class SpeakingListUpdate(BaseModel):
    reportId: int
    userId: int
class SpeakingListEntry(BaseModel):
    name:str
    surname:str
    council:str
    reportType:int
    reportTime:str
    reportApplicantInfo:str

    class Config:  # tells pydantic to convert even non dict obj to json
        orm_mode = True