from sqlalchemy.orm import Session
from typing import List
from db.models.votingQuestion import VotingQuestion

def create_voting_question(question_data: dict, db: Session):
    new_question = VotingQuestion(**question_data)
    db.add(new_question)
    db.commit()
    db.refresh(new_question)
    return new_question

def get_voting_question(question_id: int, db: Session):
    return db.query(VotingQuestion).filter(VotingQuestion.id == question_id).first()

def get_all_voting_questions(db: Session):
    return db.query(VotingQuestion).all()

def update_voting_question(question_id: int, update_data: dict, db: Session):
    db.query(VotingQuestion).filter(VotingQuestion.id == question_id).update(update_data)
    db.commit()
    return db.query(VotingQuestion).filter(VotingQuestion.id == question_id).first()

def delete_voting_question(question_id: int, db: Session):
    db.query(VotingQuestion).filter(VotingQuestion.id == question_id).delete()
    db.commit()
    
def get_voting_questions_by_conference(conference_id: int, db: Session):
    return db.query(VotingQuestion).filter(VotingQuestion.conference_id == conference_id).all()
