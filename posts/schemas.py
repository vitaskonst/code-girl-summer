from typing import Optional
from pydantic import BaseModel

class CreatePostRequest(BaseModel):
    title: str
    content: str
    author: str
    location: str


class EditPostRequest(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None
    location: Optional[str] = None