from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List
from datetime import datetime, timedelta

from db.session import engine, get_db
from db.models.user import User
from db.models.userSecret import UserSecret
from db.models.userRoleAssignment import UserRoleAssignment
from db.models.role import Role
from db.models.council import Council

"""Databaseaccessobject to get a specific user

Parameters:
    userId (int): id of the user to return
    db (Session): databaseconnection

Returns:
    User: requested user by id
"""
def get_user(userId: int, db: Session):
    return db.query(User).filter(User.id == userId).first()

"""Databaseaccessobject to get the status of a specific user

Parameters:
    email (str): email of the user to return
    db (Session): databaseconnection

Returns:
    User Status : requested user status by email
"""
def get_user_status(email: str, db: Session = Depends(get_db)):
    return db.query(User).filter(User.email == email).first().status
    

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
    return list(db.query(User).all())


"""Databaseaccessobject to create a new user

Parameters:
    user_to_create (dict): user schema that fits db model User

Returns:
    New user object or False
"""
def create_user_in_db(user_to_create, db: Session):
    if not db.query(User).filter(User.email == user_to_create.email).first():  
        newUser = User (
            email=user_to_create.email,
            firstname = user_to_create.firstname,
            lastname = user_to_create.lastname,
            councilId = user_to_create.councilId,
            birthday = user_to_create.birthday,
            status = "Inactive"
        )
        db.add(newUser)
        db.commit()
        return newUser
    else: return False


"""Databaseaccessobject to create a new user secret in db

Parameters:
    secret_to_create (dict): user secret schema that fits db model UserSecret

Returns:
    New UserSecret object
"""
def create_user_secret(secret_to_create, db: Session):
    newUserSecret =  UserSecret (
        userId = secret_to_create.userId,
        password = secret_to_create.password,
        registrationToken = secret_to_create.registrationToken,
        registrationTokenValidUntil = secret_to_create.registrationTokenValidUntil
        )
    db.add(newUserSecret)
    db.commit()
    return newUserSecret

"""Databaseaccessobject to update an existing user secret in db

Updates password, revokes token, set user status to active

Parameters:
    update_secret (dict): db schema that fits db model UserSecret for this purpose

Returns:
    None
"""
def update_user_secret(update_secret, db: Session):
    userSecretUpdate = db.query(UserSecret).filter(UserSecret.userId == update_secret.userId).first()
    userSecretUpdate.password = update_secret.password
    userSecretUpdate.registrationToken = update_secret.registrationToken
    userSecretUpdate.registrationTokenValidUntil = update_secret.registrationTokenValidUntil

    userUpdate = db.query(User).filter(User.id == update_secret.userId).first()
    userUpdate.status = "Active"

    db.commit()
    return

"""Databaseaccessobject to get an existing user by email

Parameters:
    email (str): email address of a user

Returns:
    User object or NoneType object
"""
def get_user_by_email(email: str, db: Session):
    return db.query(User).filter(User.email == email).first()

""""Databaseaccessobject to update an existing user secret registration token

Parameters:
    secret_to_change (UpdateToken)
    db

Returns:
    UserSecret object
"""
def update_token(secret_to_change, db:Session):
    updateSecretToken = db.query(UserSecret).filter(UserSecret.userId == secret_to_change.userId).first()
    updateSecretToken.registrationToken = secret_to_change.registrationToken
    updateSecretToken.registrationTokenValidUntil = secret_to_change.registrationTokenValidUntil
    db.commit()
    return updateSecretToken

""""Databaseaccessobject to get an existing user secret registration token by token

Parameters:
    token (str): Encoded JWT given as parameter

Returns:
    UserSecret object or NoneType
"""
def get_reset_token(token, db: Session):
    return db.query(UserSecret).filter(UserSecret.registrationToken == token).first()

def update_role_in_db(userId, roleId, conferenceId, db):
    #TODO: DAO
    pass

def get_users_with_roles(db: Session):
    pass