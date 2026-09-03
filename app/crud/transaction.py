from sqlalchemy.orm import Session

from app.models.transaction import Transaction
from app.models.account import Account
from app.schemas.transaction import TransactionCreate

def get_transaction(db: Session, transaction_id: int) -> Transaction | None:
    return db.query(Transaction).filter(Transaction.id == transaction_id).first()

def get_transactions_by_account(db: Session, account_id: int) -> list[Transaction]:
    return db.query(Transaction).filter(Transaction.account_id == account_id).all()

def create_transaction(db: Session, transaction: TransactionCreate) -> Transaction | None:
    db_account = db.query(Account).filter(Account.id == transaction.account_id).first()
    if db_account is None:
        return None

    if transaction.type == "withdraw" and transaction.amount > db_account.balance:
        raise ValueError("Saldo insuficiente!")
    if transaction.type == "deposit":
        db_account.balance += transaction.amount
    elif transaction.type == "withdraw":
        db_account.balance -= transaction.amount

    db_transaction = Transaction(**transaction.model_dump())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction
        