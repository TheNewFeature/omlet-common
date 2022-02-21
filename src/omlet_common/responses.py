from typing import List, Optional

from pydantic import BaseModel

from omlet_common.schemas.device import Device
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


class CreateDeviceResponse(BaseModel):
    device_id: List[int]


class GetDevicesResponse(BaseModel):
    devices: List[Device]


class GetAvailableDeviceResponse(BaseModel):
    device: Optional[Device]
