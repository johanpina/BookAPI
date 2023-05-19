from fastapi import FastAPI
from database import SessionLocal, Base, engine
from models import LibroDB

Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


app = FastAPI()

