from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.transaction import TransactionCreate, TransactionRead
from app.crud import transaction as crud_transaction

router = APIRouter(prefix="/transactions", tags=["transactions"])

@router.post("/", response_model=TransactionRead)
def create_transaction(transaction: TransactionCreate, db:Session = Depends(get_db)):
    try:
        db_transaction = crud_transaction.create_transaction(db, transaction)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_transaction

@router.get("/{transaction_id}", response_model=TransactionRead)
def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    db_transaction = crud_transaction.get_transaction(db, transaction_id)
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return db_transaction

@router.get("/account/{account_id}", response_model= list[TransactionRead])
def list_transaction_by_account(account_id: int, db: Session = Depends(get_db)):
    return crud_transaction.get_transactions_by_account(db, account_id)
    