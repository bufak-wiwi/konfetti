from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List

from db.session import get_db
from db.models.user import User
from db.models.userSecret import UserSecret
from db.models.userRoleAssignment import UserRoleAssignment
from db.models.role import Role


def get_user(userId: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.id == userId).first()

def get_user_for_login(email: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    userSecret = db.query(UserSecret).filter(UserSecret.userId == user.id).first()

    return userSecret

def get_userpermission(id: int, db: Session = Depends(get_db)):
    permission_dict = {
        "USER": True,
        "ADMIN": False,
        "COUNCIL": False,
        "ORGANIZER": False
    }
    userRoles: List[UserRoleAssignment] = db.query(UserRoleAssignment).join(Role, Role.id==UserRoleAssignment.roleId).filter(UserRoleAssignment.userId == id and UserRoleAssignment.conferenceId == None).all()
    for roleAssingment in userRoles:
        permission_dict[roleAssingment.role.name] = True
    userConferenceOrganizer: List[UserRoleAssignment] = db.query(UserRoleAssignment).filter(UserRoleAssignment.userId == id and UserRoleAssignment.conferenceId != None).all()
    if len(userConferenceOrganizer) > 0:
        permission_dict["ORGANIZER"] = True
        for roleAssingment in userConferenceOrganizer:
            permission_dict[roleAssingment.conferenceId] = True
    return permission_dict

def get_users(db: Session):
    return list(db.query(User).all())