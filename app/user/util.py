from datetime import datetime, timedelta
from typing import Dict, Union
from passlib.context import CryptContext
import jwt
from jwt.exceptions import DecodeError

from app.logger import logger
from .config import AuthConfig


def verify_password(password, hashed_password):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    return pwd_context.verify(password, hashed_password)


def get_hashed_password(password):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    return pwd_context.hash(password)


def encode_token(user_id: str, auth_config: AuthConfig) -> str:
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(hours=auth_config.TOKEN_EXPIRE_HOUR),
    }
    token = jwt.encode(payload, auth_config.JWT_SECRET, auth_config.JWT_ALGORITHM)

    return token


def decode_token(token: str, auth_config: AuthConfig) -> Union[Dict, None]:
    try:
        decoded_token = jwt.decode(
            token, auth_config.JWT_SECRET, auth_config.JWT_ALGORITHM
        )
        return decoded_token

    except DecodeError:
        logger.error("Error decoding token")
