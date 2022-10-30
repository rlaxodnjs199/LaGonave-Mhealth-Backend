from typing import Union
import uuid

from fastapi import Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.pgsql.session import get_db
from .util import get_hashed_password, verify_password
from .models import User
from .schemas import CreateUserRequestSchema


class UserDAL:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    async def create_user(self, new_user: CreateUserRequestSchema) -> User:
        user = await self.get_user_by_username(new_user.username)

        if user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists",
                headers={"WWW-Authenticate": "Bearer"},
            )

        new_user = User(
            username=new_user.username,
            role=new_user.role,
            password=get_hashed_password(new_user.password),
        )
        self.db_session.add(new_user)
        await self.db_session.commit()

        return new_user

    async def get_user_by_id(self, user_id: uuid.UUID) -> User:
        q = await self.db_session.execute(select(User).where(User.id == user_id))
        user = q.scalars().first()
        await self.db_session.commit()

        return user

    async def get_user_by_username(self, username: str) -> User:
        q = await self.db_session.execute(select(User).where(User.username == username))
        user = q.scalars().first()
        await self.db_session.commit()

        return user

    async def authenticate(self, username: str, password: str) -> Union[User, None]:
        user = await self.get_user_by_username(username)

        if not user or not verify_password(password, user.password):
            return None

        return user


def get_user_dal(db=Depends(get_db)) -> UserDAL:
    return UserDAL(db)
