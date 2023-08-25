import logging
from functools import lru_cache
from typing import Optional

from pydantic import AnyUrl

log = logging.getLogger("uvicorn")


class Settings:
    def __init__(
        self,
        environment: str = "dev",
        testing: bool = False,
        database_url: Optional[AnyUrl] = None,
    ):
        self.environment = environment
        self.testing = testing
        self.database_url = database_url


@lru_cache()
def get_settings() -> Settings:
    log.info("Loading config settings from the environment...")
    return Settings()
