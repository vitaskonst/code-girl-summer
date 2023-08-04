from typing import Optional
from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str


class EditUserRequest(BaseModel):
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
