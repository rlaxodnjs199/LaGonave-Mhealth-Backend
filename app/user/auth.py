import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from .schemas import GetUserResponseSchema
from .dal import get_user_dal, UserDAL
from .util import encode_token, decode_token
from .config import auth_config

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/login", response_model=GetUserResponseSchema)
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

    return {"access_token": access_token}


@router.get("/token", response_model=GetUserResponseSchema)
async def verify_token(
    token: str = Depends(oauth2_scheme), user_dal: UserDAL = Depends(get_user_dal)
):
    payload = decode_token(token)
    user_id = payload.get("sub")

    if isinstance(user_id, uuid.UUID):
        user = await user_dal.get_user_by_id(user_id)
        if user:
            return {"access_token": token}
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
                headers={"WWW-Authenticate": "Bearer"},
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user ID",
            headers={"WWW-Authenticate": "Bearer"},
        )
