from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import urllib.parse

# Parâmetros de conexão
usuario = "root"
senha = "Are@0051"
host = "localhost"
nome_do_banco = "filmes"

senha_codificada = urllib.parse.quote_plus(senha)
conexao_string = f"mysql+pymysql://{usuario}:{senha_codificada}@{host}/{nome_do_banco}"

engine = create_engine(conexao_string, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()