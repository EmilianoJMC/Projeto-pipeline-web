from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from backend.database.db import engine

Base = declarative_base()

class Filme(Base):
    __tablename__ = "filmes"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)
    genero = Column(String(100), nullable=False)

# Criar tabelas automaticamente
Base.metadata.create_all(bind=engine)