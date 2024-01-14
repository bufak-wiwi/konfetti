
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Schema for creating a new voting question
class CreateVotingQuestion(BaseModel):
    conference_id: int
    questionText: str
    type: str
    arrivedCouncilCount: int
    isOpen: bool
    isSecret: bool
    votingOptions: list

# Schema for updating an existing voting question
class UpdateVotingQuestion(BaseModel):
    questionText: Optional[str]
    type: Optional[str]
    arrivedCouncilCount: Optional[int]
    isOpen: Optional[bool]
    isSecret: Optional[bool]
    votingOptions: Optional[list]

# Schema for displaying a voting question
class ShowVotingQuestion(BaseModel):
    id: int
    conference_id: int
    questionText: str
    arrivedCouncilCount: int
    isOpen: bool
    isSecret: bool
    votingOptions: list
    votes: list
    result: str
    created_at: datetime
