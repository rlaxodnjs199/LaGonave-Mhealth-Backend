from fastapi import APIRouter, Depends

from .dal import UserDAL, get_user_dal
from .schemas import CreateUserRequestSchema, CreateUserResponseSchema

router = APIRouter()


@router.post("/", response_model=CreateUserResponseSchema)
async def create_user(
    new_user: CreateUserRequestSchema, user_dal: UserDAL = Depends(get_user_dal)
):
    new_user = await user_dal.create_user(new_user)

    return new_user
