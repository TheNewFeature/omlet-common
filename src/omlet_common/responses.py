from pydantic import BaseModel

from omlet_common.schemas.session import Session


class BaseResponse(BaseModel):
    message: str
    response: BaseModel


class CreateSessionResponse(BaseModel):
    session_id: int


class UpdateSessionStateResponse(BaseModel):
    session: Session


class UpdateSessionContainerResponse(BaseModel):
    session: Session


class CreateCheckpointResponse(BaseModel):
    id: int


class CreateDatasetResponse(BaseModel):
    pass


class DeleteDatasetResponse(BaseModel):
    pass
