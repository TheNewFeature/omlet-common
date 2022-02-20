from typing import Optional

from pydantic import BaseModel


class CreateArtifactRequest(BaseModel):
    object_name: str
    etag: str
    version_id: Optional[str] = None


class CreateSessionRequest(BaseModel):
    artifact: CreateArtifactRequest
    dataset: str


class UpdateSessionStateRequest(BaseModel):
    state: str


class UpdateSessionContainerRequest(BaseModel):
    container_id: str


class CreateDatasetRequest(BaseModel):
    display_name: str
    object_name: str
    etag: str


class DeleteDatasetRequest(BaseModel):
    object_name: str
