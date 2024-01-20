from pydantic import BaseModel

class UserRoleAssignment(BaseModel):
   userId: int
   roleId: int
   conferenceId: int
   