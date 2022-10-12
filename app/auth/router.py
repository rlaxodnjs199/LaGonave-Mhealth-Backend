from fastapi import APIRouter, Depends
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession

from .dependencies import get_db_session

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def test_db(db: AsyncSession = Depends(get_db_session)):
    return True
