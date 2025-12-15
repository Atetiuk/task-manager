from pydantic import BaseModel

class KategoriaCreate(BaseModel):
    nazwa: str

class Kategoria(KategoriaCreate):
    id: int
    model_config = {"from_attributes": True}

class ZadanieCreate(BaseModel):
    tytul: str
    opis: str
    kategoria_id: int

class Zadanie(ZadanieCreate):
    id: int
    model_config = {"from_attributes": True}
