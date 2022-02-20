from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class PydanticTimeMixin:
    created_at: datetime
    last_modified_at: datetime


class Artifact(PydanticTimeMixin, BaseModel):
    id: Optional[int] = None
    etag: str
    object_name: str
    version_id: Optional[str]


class Checkpoint(PydanticTimeMixin, BaseModel):
    id: Optional[int] = None
    session_id: int
    episode: int
    display_name: str
    etag: str
    object_name: str


class Dataset(PydanticTimeMixin, BaseModel):
    id: Optional[int] = None
    display_name: str
    etag: str
    object_name: str


class Session(PydanticTimeMixin, BaseModel):
    id: Optional[int] = None
    name: str
    user_id: int
    artifact_id: int
    dataset_id: int
    device_id: int
    container_id: str
    state: str
