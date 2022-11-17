from uuid import UUID

from fastapi import APIRouter, Depends

from .dal import UserDAL, get_user_dal
from .schemas import (
    CreateUserRequestSchema,
    CreateUserResponseSchema,
    GetUserResponseSchema,
)

router = APIRouter()


@router.post("/", response_model=CreateUserResponseSchema)
async def create_user(
    new_user: CreateUserRequestSchema, user_dal: UserDAL = Depends(get_user_dal)
):
    new_user = await user_dal.create_user(new_user)

    return new_user


@router.get("/", response_model=GetUserResponseSchema)
async def get_user(user_id: UUID, user_dal: UserDAL = Depends(get_user_dal)):
    user = await user_dal.get_user_by_id(user_id)

    return user
