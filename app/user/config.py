from functools import lru_cache
from pydantic import BaseSettings


class AuthConfig(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    JWT_SECRET: str
    JWT_ALGORITHM: str
    TOKEN_EXPIRE_HOUR: int


@lru_cache()
def get_auth_config() -> AuthConfig:
    return AuthConfig()


auth_config = get_auth_config()
