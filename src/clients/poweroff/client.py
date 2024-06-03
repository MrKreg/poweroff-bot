from datetime import datetime

import httpx

from clients.poweroff.models import Status, CheckSchedulesResponse, Schedule


class PowerOffClient:
    BASE_URL = "https://poweroff.if.ua/"

    @classmethod
    async def get_status(cls) -> Status:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{cls.BASE_URL}/status")
            return Status(**response.json())

    @classmethod
    async def check_schedules(cls, date: datetime) -> CheckSchedulesResponse:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{cls.BASE_URL}/check_schedules",
                params={"date": date.strftime("%Y-%m-%d")},
            )
            return CheckSchedulesResponse(**response.json())

    @classmethod
    async def get_schedule(cls, date: datetime) -> Schedule:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{cls.BASE_URL}/schedule",
                params={"date": date.strftime("%Y-%m-%d")},
            )
            return Schedule(**response.json())
