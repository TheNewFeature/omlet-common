from typing import List, Optional

from pydantic import BaseModel


class Device(BaseModel):
    id: int = -1
    name: str
    uuid: str
    total_global_memory: int
    machine_id: int = -1

    class Config:
        orm_mode = True


class Machine(BaseModel):
    id: int = -1
    name: str

    class Config:
        orm_mode = True
