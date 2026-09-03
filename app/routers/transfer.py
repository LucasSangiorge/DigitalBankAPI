from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.transfer import TransferCreate, TransferRead
from app.crud import transfer as crud_transfer

router = APIRouter(prefix="/transfers", tags=["transfers"])

@router.post("/", response_model=TransferRead)
def create_transfer(transfer: TransferCreate, db: Session = Depends(get_db)):
    try:
        db_transfer = crud_transfer.create_transfer(db, transfer)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    if db_transfer is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return db_transfer

@router.get("/{transfer_id}", response_model=TransferRead)
def read_transfer(transfer_id: int, db: Session = Depends(get_db)):
    db_transfer = crud_transfer.get_transfer(db, transfer_id)
    if db_transfer is None:
        raise HTTPException(status_code=404, detail="Transfer not found")
    return db_transfer