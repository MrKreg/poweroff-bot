from datetime import datetime

from pydantic import BaseModel


class State(BaseModel):
    id: int
    name: str
    name_en: str
    alert: bool
    changed: datetime


class Status(BaseModel):
    last_updated: datetime
    state: State


class CheckSchedulesResponse(BaseModel):
    tomorrow_data: bool
    yesterday_data: bool


class Range(BaseModel):
    id: int
    date: datetime
    created_at: datetime
    updated_at: datetime
    name: str
    off: list[tuple[int, int]]
    on: list[tuple[int, int]]
    maybe: list[tuple[int, int]]


class Schedule(BaseModel):
    ranges: list[list[str]]
