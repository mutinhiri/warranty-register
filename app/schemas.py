from pydantic import BaseModel
from datetime import datetime

class WarrantyCreate(BaseModel):
    asset_id: str
    asset_serial: str
    registered_by: str
    # asset_name: str

class WarrantyOut(BaseModel):
    id: int
    asset_id: str
    # asset_name: str
    asset_serial: str
    registered_by: str
    registered_at: datetime

    model_config = {
         "from_attributes": True
    }
       
