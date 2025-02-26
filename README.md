## Projeto Pipeline Web

Este projeto é uma API web desenvolvida com FastAPI para gerenciar uma coleção de filmes. A API permite adicionar novos filmes e listar todos os filmes no banco de dados. Atualmente, estamos utilizando SQLAlchemy para interagir com um banco de dados MySQL.

### Estrutura do Projeto

backend/:
  - main.py: Ponto de entrada da aplicação FastAPI.
    
  - api/routes.py: Define as rotas da API.

  - auth/security.py: Funções de segurança e criptografia.

database/:

  - crud.py: Funções CRUD para o banco de dados.

  - db.py: Configuração e conexão com o banco de dados.

  - models.py: Definição dos modelos de dados.

services/

  - extract.py: Script para extrair dados populares de filmes.

frontend/

  - app.py: Requisição para da API para frontend

### Funcionalidades
Listar Filmes: Obtenha uma lista de todos os filmes no banco de dados.

Adicionar Filme: Adicione um novo filme ao banco de dados.

Atualização Automática: Um script em execução agendada para atualizar os dados dos filmes.

### Status
Em progresso: Estamos atualmente trabalhando em diversas funcionalidades e melhorias. Sinta-se à vontade para explorar o código e contribuir!
