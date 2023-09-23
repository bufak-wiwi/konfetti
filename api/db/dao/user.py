from sqlalchemy.orm import Session
from fastapi import Depends

from db.session import get_db
from db.models.user import User
from db.models.userSecret import UserSecret


def get_user(userId: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.id == userId).first()

def get_user_for_login(email: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    userSecret = db.query(UserSecret).filter(UserSecret.userId == user.id).first()

    return userSecret

def get_userpermission(id: int):
    permission_dict = {
        "USER": True,
        "ADMIN": False,
        "COUNCIL": False,
    }
    # ToDo find all permissions
    return permission_dict

def get_users(db: Session):
    return list(db.query(User).all())