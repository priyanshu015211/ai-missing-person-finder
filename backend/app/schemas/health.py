from typing import Literal

from pydantic import BaseModel


class ApiHealthResponse(BaseModel):
    status: Literal["ok"]
    service: str
    version: str


class DatabaseHealthResponse(BaseModel):
    status: Literal["ok"]
    database: Literal["connected"]
