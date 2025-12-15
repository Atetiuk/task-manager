from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..crud import create_kategoria, get_kategorie
from ..schemas import KategoriaCreate, Kategoria
from ..crud import create_kategoria, get_kategorie, delete_kategoria


router = APIRouter(prefix="/kategorie", tags=["kategorie"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Kategoria)
def add_kategoria(data: KategoriaCreate, db: Session = Depends(get_db)):
    return create_kategoria(db, data)

@router.get("/", response_model=list[Kategoria])
def list_kategorie(db: Session = Depends(get_db)):
    return get_kategorie(db)

@router.delete("/{kategoria_id}")
def remove_kategoria(kategoria_id: int, db: Session = Depends(get_db)):
    return delete_kategoria(db, kategoria_id)
