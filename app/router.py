from fastapi import APIRouter
from app.user.auth import router as auth_router
from app.user.endpoints import router as user_router

router = APIRouter(prefix="/api")
router.include_router(auth_router, prefix="/auth", tags=["Auth"])
router.include_router(user_router, prefix="/users", tags=["User"])
