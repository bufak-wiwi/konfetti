
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Schema for creating a new voting answer
class CreateVotingAnswer(BaseModel):
    question_id: int
    council_id: int
    vote: str

# Schema for updating an existing voting answer
class UpdateVotingAnswer(BaseModel):
    vote: str

# Schema for displaying a voting answer
class ShowVotingAnswer(BaseModel):
    id: int
    question_id: int
    council_id: int
    priority: int
    vote: str
    # created_at: datetime
    # updated_at: Optional[datetime]
