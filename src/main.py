from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.database import SessionLocal, Base, engine

# Инициализация таблиц в БД
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency для работы с БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI Backend!"}
