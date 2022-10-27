from functools import lru_cache
from logging import getLogger
from logging.config import dictConfig
from pydantic import BaseModel


class LogConfig(BaseModel):
    """Logging configuration"""

    LOGGER_NAME: str = "lagonave-fastapi"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = "DEBUG"

    # Logging config
    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers = {
        "lagonave-fastapi": {"handlers": ["default"], "level": LOG_LEVEL},
    }


@lru_cache
def get_logger():
    dictConfig(LogConfig().dict())
    logger = getLogger("lagonave-fastapi")

    return logger


logger = get_logger()
