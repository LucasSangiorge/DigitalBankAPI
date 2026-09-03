from sqlalchemy import Column,Integer,Float,ForeignKey,DateTime
from sqlalchemy.sql import func
from app.database import Base

class Transfer(Base):
    __tablename__ = "transfers"

    id = Column(Integer, primary_key=True, index=True)
    from_account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    to_account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    amount = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
