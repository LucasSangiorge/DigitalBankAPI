from sqlalchemy import Column,Integer,String,Float,ForeignKey,DateTime
from sqlalchemy.sql import func
from app.database import Base

class Transaction(Base):
    __tablename__= "transactions"

    id = Column(Integer, primary_key=True, index=True)
    account_id= Column(Integer,ForeignKey("accounts.id"), nullable=False)
    type= Column(String, nullable=False)
    amount= Column(Float, nullable=False)
    created_at= Column(DateTime(timezone=True), server_default=func.now())
    