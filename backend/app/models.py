from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Kategoria(Base):
    __tablename__ = "kategorie"
    id = Column(Integer, primary_key=True)
    nazwa = Column(String, unique=True)

class Zadanie(Base):
    __tablename__ = "zadania"
    id = Column(Integer, primary_key=True)
    tytul = Column(String)
    opis = Column(String)
    kategoria_id = Column(Integer, ForeignKey("kategorie.id"))
    kategoria = relationship("Kategoria")
