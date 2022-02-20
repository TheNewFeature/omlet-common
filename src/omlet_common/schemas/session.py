from typing import Optional

from pydantic import BaseModel


class Session(BaseModel):
    id: Optional[int] = None
    name: str = ''
    user_id: int = 0
    artifact_id: int = 0
    dataset_id: int = 0
    device_id: int = 0
    container_id: Optional[str] = None
    state: Optional[str] = None

    class Config:
        orm_mode = True


class SessionStatePatch(BaseModel):
    state: str


class SessionContainerIdPatch(BaseModel):
    container_id: str
