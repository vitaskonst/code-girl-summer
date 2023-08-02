from posts.schemas import CreatePostRequest, EditPostRequest
from fastapi import HTTPException, APIRouter


router = APIRouter()


@router.get('')
def get_posts():
    return posts


@router.post('')
def create_post(post: CreatePostRequest):
    global last_added_post_id
    new_id = last_added_post_id + 1
    posts[new_id] = post
    last_added_post_id = new_id
    return new_id


@router.get('/{id}')
def get_post(id: int):
    if id not in posts:
        raise HTTPException(
            status_code=404, detail=f'No post with id {id} was found')

    return posts[id]


@router.put('/{id}')
def edit_post(id: int, post: EditPostRequest):
    if id not in posts:
        raise HTTPException(
            status_code=404, detail=f'No post with id {id} was found')

    for key, value in post.dict().items():
        if value is not None:
            posts[id][key] = value

    return id


@router.delete('/{id}')
def edit_post(id: int):
    if id not in posts:
        raise HTTPException(
            status_code=404, detail=f'No post with id {id} was found')

    del posts[id]

    return id
