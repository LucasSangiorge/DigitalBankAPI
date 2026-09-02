from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.account import AccountCreate, AccountRead, AccountUpdate
from app.crud import account as crud_account

router = APIRouter(prefix="/accounts", tags=["accounts"])

@router.post("/", response_model=AccountRead)
def create_account(account: AccountCreate, db: Session = Depends(get_db)):
    return crud_account.create_account(db, account)

@router.get("/{account_id}", response_model=AccountRead)
def read_account(account_id: int, db: Session = Depends(get_db)):
    db_account = crud_account.get_account(db, account_id)
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account

@router.get("/", response_model=list[AccountRead])
def list_accounts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_account.get_accounts(db, skip, limit)

@router.put("/{account_id}", response_model=AccountRead)
def update_account(account_id: int, account: AccountUpdate, db: Session = Depends(get_db)):
    db_account = crud_account.update_account(db, account_id, account)
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account

@router.delete("/{account_id}", response_model=AccountRead)
def delete_account(account_id: int, db: Session = Depends(get_db)):
    db_account = crud_account.delete_account(db, account_id)
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_account