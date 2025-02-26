from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from backend.database.db import get_db
from backend.database.crud import criar_filme, listar_filmes

class Filme(BaseModel):
    titulo: str
    genero: str

router = APIRouter()

@router.get("/filmes")
def get_filmes(db: Session = Depends(get_db)):
    return listar_filmes(db)

@router.post("/filmes")
def add_filme(filme: Filme, db: Session = Depends(get_db)):
    print(f"Recebendo filme: {filme.titulo}, {filme.genero}")
    return criar_filme(db, filme.titulo, filme.genero)
