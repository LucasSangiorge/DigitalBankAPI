from sqlalchemy.orm import Session

from app.models.transfer import Transfer
from app.models.account import Account
from app.schemas.transfer import TransferCreate

def get_transfer(db: Session, transfer_id: int) -> Transfer | None:
    return db.query(Transfer).filter(Transfer.id == transfer_id).first()

def create_transfer(db: Session, transfer: TransferCreate) -> Transfer | None:
    from_account = db.query(Account).filter(Account.id == transfer.from_account_id).first()
    to_account = db.query(Account).filter(Account.id == transfer.to_account_id).first()

    if from_account is None or to_account is None:
        return None

    if transfer.from_account_id == transfer.to_account_id:
        raise ValueError("Não é possível transferir para a mesma conta")

    if transfer.amount > from_account.balance:
        raise ValueError("Saldo insuficiente")

    from_account.balance -= transfer.amount
    to_account.balance += transfer.amount

    db_transfer = Transfer(**transfer.model_dump())
    db.add(db_transfer)
    db.commit()
    db.refresh(db_transfer)
    return db_transfer