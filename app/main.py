from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routers import account
from app.routers import transaction
from app.routers import transfer

Base.metadata.create_all(bind=engine)

app = FastAPI(title="DigitalBank API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(account.router)
app.include_router(transaction.router)
app.include_router(transfer.router)
