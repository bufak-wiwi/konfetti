
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from db.session import get_db
from db.dao.votingQuestion import (
    create_voting_question,
    get_voting_question,
    get_all_voting_questions,
    update_voting_question,
    delete_voting_question,
    get_voting_questions_by_conference,
)
from endpoints.schemas.votingQuestion import CreateVotingQuestion, UpdateVotingQuestion, ShowVotingQuestion

router = APIRouter()

@router.post("/voting_questions/", response_model=ShowVotingQuestion)
def create_question(question_data: CreateVotingQuestion, db: Session = Depends(get_db)):
    return create_voting_question(question_data.dict(), db)

@router.get("/voting_questions/{question_id}", response_model=ShowVotingQuestion)
def read_question(question_id: int, db: Session = Depends(get_db)):
    question = get_voting_question(question_id, db)
    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return question

@router.get("/voting_questions/", response_model=List[ShowVotingQuestion])
def read_questions(db: Session = Depends(get_db)):
    return get_all_voting_questions(db)

@router.get("/voting_questions/conference/{conference_id}", response_model=List[ShowVotingQuestion])
def read_questions_by_conference(conference_id: int, db: Session = Depends(get_db)):
    return get_voting_questions_by_conference(conference_id, db)

@router.put("/voting_questions/{question_id}", response_model=ShowVotingQuestion)
def update_question(question_id: int, update_data: UpdateVotingQuestion, db: Session = Depends(get_db)):
    return update_voting_question(question_id, update_data.dict(), db)

@router.post("/voting_questions/{question_id}/openQuestion/", response_model=ShowVotingQuestion)
def open_question(question_id: int, db: Session = Depends(get_db)):
    update_data = {"isOpen": True}
    return update_voting_question(question_id, update_data, db)

@router.post("/voting_questions/{question_id}/closeQuestion/", response_model=ShowVotingQuestion)
def close_question(question_id: int, db: Session = Depends(get_db)):
    update_data = {"isOpen": False}
    return update_voting_question(question_id, update_data, db)

@router.delete("/voting_questions/{question_id}")
def delete_question(question_id: int, db: Session = Depends(get_db)):
    delete_voting_question(question_id, db)
    return {"message": "Question deleted successfully"}
