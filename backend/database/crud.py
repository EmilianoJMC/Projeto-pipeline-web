from sqlalchemy.orm import Session
from backend.database.models import Filme

def criar_filme(db: Session, titulo: str, genero: str):
    novo_filme = Filme(titulo=titulo, genero=genero)
    db.add(novo_filme)
    db.commit()
    db.refresh(novo_filme)
    return novo_filme

def listar_filmes(db: Session):
    return db.query(Filme).all()