from sqlalchemy.orm import Session

from app.models.account import Account
from app.schemas.account import AccountCreate, AccountUpdate

def get_account(db: Session, account_id: int) -> Account | None:
    return db.query(Account).filter(Account.id == account_id).first()

def create_account( db: Session, account: AccountCreate) ->Account:
    db_account = Account(**account.model_dump())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

def get_accounts(db: Session, skip: int = 0, limit: int= 100) -> list[Account]:
    return db.query(Account).offset(skip).limit(limit).all()

def get_account_by_number(db:Session, account_number: str) -> Account | None:
    return db.query(Account).filter(Account.account_number == account_number).first()

def update_account(db: Session, account_id: int, account: AccountUpdate) -> Account | None:
    db_account =  get_account(db, account_id)
    if db_account is None:
        return None

    update_data = account.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_account, field, value)
    db.commit()
    db.refresh(db_account)
    return db_account

def delete_account(db:Session, account_id: int) -> Account | None:
    db_account = get_account(db, account_id)
    if db_account is None:
        return None

    db.delete(db_account)
    db.commit()
    return db_account