from typing import Optional, List
from pydantic import BaseModel


class CreatePostRequest(BaseModel):
    title: str
    content: str
    author: str
    location: str
    image_urls: List[str]


class EditPostRequest(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None
    location: Optional[str] = None
    image_urls: List[str] = None
