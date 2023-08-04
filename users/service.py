from users.schemas import CreateUserRequest, EditUserRequest
from database import database
from sqlalchemy import insert, select, update, delete
from database import users
from fastapi import HTTPException
from users.security import hash_password


async def get_user_by_username(username: str):
    select_query = select(users).where(users.columns.username == username)

    return await database.fetch_one(select_query)


async def create_user(user: CreateUserRequest):
    user_db = await get_user_by_username(user.username)
    if user_db:
        raise HTTPException(status_code=400, detail="Username already exists")

    user.password = hash_password(user.password)

    insert_query = insert(users).values(
        user.dict()
    ).returning(users.columns.id)

    return await database.fetch_one(insert_query)


async def get_users():
    # select_query = 'SELECT id, username, first_name, last_name FROM users'
    select_query = select(users.columns.id, users.columns.username,
                          users.columns.first_name, users.columns.last_name)

    return await database.fetch_all(select_query)


async def get_user_by_id(user_id: int):
    # select_query = f'SELECT * FROM users WHERE id={user_id}'
    select_query = select(users.columns.id, users.columns.username, users.columns.first_name,
                          users.columns.last_name).where(users.columns.id == user_id)

    user = await database.fetch_one(select_query)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")

    return user


async def edit_user(user_id: int, user: EditUserRequest):
    user_db_by_id = await get_user_by_id(user_id)
    if not user_db_by_id:
        raise HTTPException(status_code=404, detail="user not found")

    if user.username and user_db_by_id["username"] != user.username:
        user_db = await get_user_by_username(user.username)
        if user_db:
            raise HTTPException(
                status_code=400, detail="Username already exists")

    # UPDATE users SET , content = 'content'
    update_query = (
        update(users)
        .values(user.dict(exclude_none=True))
        .where(users.columns.id == user_id)
        .returning(users)
    )
    return await database.fetch_one(update_query)


async def delete_user(user_id: int):
    delete_query = delete(users).where(users.columns.id == user_id)

    return await database.execute(delete_query)
