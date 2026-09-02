from fastapi import FastAPI

from app.database import Base, engine
from app.routers import account

Base.metadata.create_all(bind=engine)

app = FastAPI(title="DigitalBank API")

app.include_router(account.router)
