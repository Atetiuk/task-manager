from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..crud import create_zadanie, get_zadania
from ..schemas import ZadanieCreate, Zadanie

router = APIRouter(prefix="/zadania", tags=["zadania"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Zadanie)
def add_zadanie(data: ZadanieCreate, db: Session = Depends(get_db)):
    return create_zadanie(db, data)

@router.get("/", response_model=list[Zadanie])
def list_zadania(db: Session = Depends(get_db)):
    return get_zadania(db)
