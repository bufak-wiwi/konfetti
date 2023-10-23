from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List

from db.session import get_db
from db.models.user import User
from db.models.userSecret import UserSecret
from db.models.userRoleAssignment import UserRoleAssignment
from db.models.role import Role

"""Databaseaccessobject to get a specific user

Parameters:
    userId (int): id of the user to return
    db (Session): databaseconnection

Returns:
    User: requested user by id
"""
def get_user(userId: int, db: Session):
    return db.query(User).filter(User.id == userId).first()

"""Databaseaccessobject to get a specific user for login

Parameters:
    email (str): email of the user to return
    db (Session): databaseconnection

Returns:
    User: requested usersecrets by email
"""
def get_user_for_login(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    userSecret = db.query(UserSecret).filter(UserSecret.userId == user.id).first()

    return userSecret

"""Databaseaccessobject to get all permissions of a specific user
lookup the user permission roles
adds organizer role if user is organizer of one conference
adds the id of each conference for which the user was/is organzier

Parameters:
    id (int): id of the user
    db (Session): databaseconnection

Returns:
    dict: representation of the userpermissions
"""
def get_userpermission(id: int, db: Session):
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

"""Databaseaccessobject to get all users

Parameters:
    db (Session): databaseconnection

Returns:
    List[User]: list of all users
"""
def get_users(db: Session):
    return db.query(User).all()