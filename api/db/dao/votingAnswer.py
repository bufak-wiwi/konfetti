
from sqlalchemy.orm import Session
from db.models.votingAnswer import VotingAnswer

def create_voting_answer(answer_data: dict, db: Session):
    new_answer = VotingAnswer(**answer_data)
    db.add(new_answer)
    db.commit()
    db.refresh(new_answer)
    return new_answer

def get_voting_answer(answer_id: int, db: Session):
    return db.query(VotingAnswer).filter(VotingAnswer.id == answer_id).first()

def get_all_voting_answers(db: Session):
    return db.query(VotingAnswer).all()

def get_voting_answers_by_question(question_id: int, db: Session):
    return db.query(VotingAnswer).filter(VotingAnswer.question_id == question_id).all()

def update_voting_answer(answer_id: int, update_data: dict, db: Session):
    db.query(VotingAnswer).filter(VotingAnswer.id == answer_id).update(update_data)
    db.commit()
    return db.query(VotingAnswer).filter(VotingAnswer.id == answer_id).first()

def delete_voting_answer(answer_id: int, db: Session):
    db.query(VotingAnswer).filter(VotingAnswer.id == answer_id).delete()
    db.commit()
