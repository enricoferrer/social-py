# social-py

**social-py** é um pequeno projeto de aprendizado que eu criei para me familiarizar com APIs RESTful em Python. Serve como meu _playground_ para experimentar FastAPI, SQLAlchemy, migrações com Alembic e boas práticas de estrutura de código.

Este repositório não é destinado a produção; foi desenvolvido com foco educacional e para me ajudar a consolidar conhecimentos sobre construção de serviços web em Python.

## Funcionalidades básicas

- CRUD para usuários, postagens e comentários
- Estrutura modular com routers, serviços, repositórios e schemas
- Banco de dados SQLite (configurável) gerenciado via SQLAlchemy
- Migrações suportadas pelo Alembic

## Iniciando o projeto

1. **Criar e ativar um ambiente virtual** (recomendado):

   ```bash
   python -m venv venv
   # Windows PowerShell
   .\venv\Scripts\Activate.ps1
   # ou Bash
   source venv/bin/activate
   ```

2. **Instalar dependências**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar variáveis de ambiente** (opcional):
   - Crie um arquivo `.env` na raiz e adicione configurações como `DATABASE_URL` se quiser usar outro banco.

4. **Rodar migrações** para preparar o banco de dados:

   ```bash
   alembic upgrade head
   ```

5. **Iniciar o servidor de desenvolvimento**:

   ```bash
   uvicorn app.main:app --reload
   ```

6. **Acessar a documentação interativa** em `http://localhost:8000/docs` para testar endpoints.

---

> ⚠️ Lembre-se: este projeto é minha ferramenta de aprendizado. Sinta-se à vontade para modificar, quebrar e reconstruir coisas enquanto exploro o ecossistema de APIs Python.
