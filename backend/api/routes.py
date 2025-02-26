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
    print(f"Recebendo filme: {filme.titulo}, {filme.genero}")  # Log de debug
    novo_filme = criar_filme(db, filme.titulo, filme.genero)
    print(f"Filme salvo no banco: {novo_filme}")  # Verifica se salvou
    return {"mensagem": "Filme adicionado com sucesso!", "filme": novo_filme}
