from fastapi import FastAPI, HTTPException, Request
from typing import Dict, Optional
from pydantic import BaseModel

# title
# content
# location
# author

app = FastAPI()

posts = {}
last_added_post_id = -1

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


@app.get('/posts')
def get_posts():
    return posts


@app.post('/posts')
def create_post(post: CreatePostRequest):
    global last_added_post_id
    new_id = last_added_post_id + 1
    posts[new_id] = post
    last_added_post_id = new_id
    return new_id


@app.get('/post/{id}')
def get_post(id: int):
    if id not in posts: 
        raise HTTPException(status_code=404, detail=f'No post with id {id} was found')
    
    return posts[id]


@app.put('/post/{id}')
def edit_post(id: int, post: EditPostRequest):
    if id not in posts: 
        raise HTTPException(status_code=404, detail=f'No post with id {id} was found')
    
    for key, value in post.dict().items():
        if value is not None:
            posts[id][key] = value

    return id

@app.delete('/post/{id}')
def edit_post(id: int):
    if id not in posts: 
        raise HTTPException(status_code=404, detail=f'No post with id {id} was found')
    
    del posts[id]

    return id
