from sqlalchemy.orm import Session
from .models import Kategoria, Zadanie
from .schemas import KategoriaCreate, ZadanieCreate

def create_kategoria(db: Session, data: KategoriaCreate):
    k = Kategoria(nazwa=data.nazwa)
    db.add(k)
    db.commit()
    db.refresh(k)
    return k

def get_kategorie(db: Session):
    return db.query(Kategoria).all()

def delete_kategoria(db: Session, kategoria_id: int):
    k = db.query(Kategoria).filter(Kategoria.id == kategoria_id).first()
    if k:
        db.delete(k)
        db.commit()
    return k

def create_zadanie(db: Session, data: ZadanieCreate):
    z = Zadanie(**data.model_dump())
    db.add(z)
    db.commit()
    db.refresh(z)
    return z

def get_zadania(db: Session):
    return db.query(Zadanie).all()

def delete_zadanie(db: Session, zadanie_id: int):
    z = db.query(Zadanie).filter(Zadanie.id == zadanie_id).first()
    if z:
        db.delete(z)
        db.commit()
    return z
