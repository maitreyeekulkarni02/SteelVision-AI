from pydantic import BaseModel


class MachineResponse(BaseModel):
    machine_id: str
    machine_name: str
    machine_type: str
    location: str
    current_health: int
    status: str

    class Config:
        from_attributes = True
