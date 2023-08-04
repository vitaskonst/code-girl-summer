from users.schemas import CreateUserRequest, EditUserRequest
from fastapi import HTTPException, APIRouter
import time
from users import service

router = APIRouter()


@router.get('')
async def get_users():
    return await service.get_users()


@router.post('')
async def create_user(user: CreateUserRequest):
    return await service.create_user(user)


@router.get('/{id}')
async def get_user(id: int):
    return await service.get_user_by_id(id)


@router.put('/{id}')
async def edit_user(id: int, user_data: EditUserRequest):
    return await service.edit_user(id, user_data)


@router.delete('/{id}')
async def delete_user(id: int):
    await service.delete_user(id)

    return {"message": "ok, deleted"}
