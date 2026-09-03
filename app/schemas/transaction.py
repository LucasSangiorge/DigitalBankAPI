from pydantic import BaseModel, ConfigDict
from datetime import datetime

class TransactionBase(BaseModel):
    account_id: int
    type: str
    amount: float

class TransactionCreate(TransactionBase):
    pass

class TransactionRead(TransactionBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime

