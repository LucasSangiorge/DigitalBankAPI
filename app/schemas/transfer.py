from pydantic import BaseModel, ConfigDict
from datetime import datetime

class TransferBase(BaseModel):
    from_account_id: int
    to_account_id: int
    amount: float

class TransferCreate(TransferBase):
    pass

class TransferRead(TransferBase):
    model_config= ConfigDict(from_attributes=True)
    id: int
    created_at: datetime