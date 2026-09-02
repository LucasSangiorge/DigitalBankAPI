from sqlalchemy import Column,Integer, String, Float
from app.database import Base

class Account(Base):
    __tablename__="accounts"

    id = Column(Integer,primary_key=True, index=True)
    owner_name = Column(String, nullable=False)
    account_number = Column(String, unique=True,index=True, nullable=False)
    balance = Column(Float,nullable=False,default=0.0)