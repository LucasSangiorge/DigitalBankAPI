from pydantic import BaseModel, ConfigDict

class AccountBase(BaseModel):
    owner_name: str
    account_number: str

class AccountCreate(AccountBase):
    pass 

class AccountRead(AccountBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    balance: float

class AccountUpdate(BaseModel):
    owner_name: str | None = None