from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from .schemas import LoginResponseSchema
from .dal import get_user_dal, UserDAL
from .util import encode_token
from .config import auth_config

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


@router.post("/login", response_model=LoginResponseSchema)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    user_dal: UserDAL = Depends(get_user_dal),
):
    user = await user_dal.authenticate(form_data.username, form_data.password)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = encode_token(user.username, auth_config)

    return {"access_token": access_token, "user_id": user.id}
