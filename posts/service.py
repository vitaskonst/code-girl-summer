from posts.schemas import CreatePostRequest, EditPostRequest
from database import database
from sqlalchemy import insert, select, update, delete
from database import posts
from fastapi import HTTPException


async def create_post(post: CreatePostRequest):
    # insert_query = f'INSERT INTO posts (title, content, author, location) VALUES (\'{post.title}\', \'{post.content}\', \'{post.author}\', \'{post.location}\')'
    insert_query = insert(posts).values(
        post.dict()
    ).returning(posts.columns.id)

    return await database.fetch_one(insert_query)


async def get_posts():
    # select_query = 'SELECT * FROM posts'
    select_query = select(posts)

    return await database.fetch_all(select_query)


async def get_post_by_id(post_id: int):
    # select_query = f'SELECT * FROM posts WHERE id={post_id}'
    select_query = select(posts).where(posts.columns.id == post_id)

    post = await database.fetch_one(select_query)
    if not post:
        raise HTTPException(status_code=404, detail="post not found")

    return post


async def edit_post(post_id: int, post: EditPostRequest):
    post_db = await get_post_by_id(post_id)
    if not post_db:
        raise HTTPException(status_code=404, detail="post not found")

    # UPDATE posts SET , content = 'content'
    update_query = (
        update(posts)
        .values(post.dict(exclude_none=True))
        .where(posts.c.id == post_id)
        .returning(posts)
    )
    return await database.fetch_one(update_query)


async def delete_post(post_id: int):
    delete_query = delete(posts).where(posts.columns.id == post_id)

    return await database.execute(delete_query)
