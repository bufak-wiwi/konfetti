
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from db.session import get_db
from db.dao.votingAnswer import (
    create_voting_answer,
    get_voting_answer,
    get_all_voting_answers,
    update_voting_answer,
    delete_voting_answer,
)
from db.models.votingAnswer import VotingAnswer
from api.endpoints.schemas.votingAnswer import (
    CreateVotingAnswer,
    UpdateVotingAnswer,
    ShowVotingAnswer,
)

router = APIRouter()

@router.post("/voting_answers/", response_model=ShowVotingAnswer)
def create_answer(answer_data: CreateVotingAnswer, db: Session = Depends(get_db)):
    return create_voting_answer(answer_data.dict(), db)

@router.get("/voting_answers/{answer_id}", response_model=ShowVotingAnswer)
def read_answer(answer_id: int, db: Session = Depends(get_db)):
    answer = get_voting_answer(answer_id, db)
    if answer is None:
        raise HTTPException(status_code=404, detail="Answer not found")
    return answer

@router.get("/voting_answers/", response_model=List[ShowVotingAnswer])
def read_answers(db: Session = Depends(get_db)):
    return get_all_voting_answers(db)

@router.put("/voting_answers/{answer_id}", response_model=ShowVotingAnswer)
def update_answer(answer_id: int, update_data: UpdateVotingAnswer, db: Session = Depends(get_db)):
    return update_voting_answer(answer_id, update_data.dict(), db)

@router.delete("/voting_answers/{answer_id}")
def delete_answer(answer_id: int, db: Session = Depends(get_db)):
    delete_voting_answer(answer_id, db)
    return {"message": "Answer deleted successfully"}
