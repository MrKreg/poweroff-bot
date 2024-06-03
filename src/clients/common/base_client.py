from abc import ABC
from datetime import datetime
from typing import Any


class BaseClient(ABC):
    BASE_URL = NotImplemented

    @classmethod
    async def get_status(cls) -> Any:
        raise NotImplementedError

    @classmethod
    async def get_schedule(cls, date: datetime) -> Any:
        raise NotImplementedError
