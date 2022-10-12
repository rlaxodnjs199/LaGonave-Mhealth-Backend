from functools import lru_cache
from pydantic import BaseSettings, PostgresDsn


class AppSettings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    DATABASE_URL: PostgresDsn


@lru_cache()
def get_settings() -> AppSettings:
    return AppSettings()


settings = get_settings()
