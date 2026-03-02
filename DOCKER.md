# Social API - Docker Setup

Este projeto está configurado para rodar com Docker Compose, incluindo banco de dados PostgreSQL e migrations automáticas.

## Pré-requisitos

- Docker
- Docker Compose

## Como usar

### 1. Iniciar os containers

```bash
docker-compose up --build
```

Isso irá:
- Criar e iniciar o container do PostgreSQL
- Criar e iniciar o container da aplicação FastAPI
- Executar automaticamente as migrations do Alembic
- Iniciar o servidor na porta 8000 em modo reload (para desenvolvimento)

### 2. Acessar a aplicação

- API: http://localhost:8000
- Documentação Swagger: http://localhost:8000/docs
- Documentação ReDoc: http://localhost:8000/redoc

### 3. Parar os containers

```bash
docker-compose down
```

Para remover os volumes (dados do banco):
```bash
docker-compose down -v
```

## Estrutura do projeto

- `docker-compose.yml` - Configuração dos containers (PostgreSQL + FastAPI)
- `Dockerfile` - Imagem da aplicação FastAPI
- `alembic/` - Scripts de migration do banco de dados
  - `versions/` - Arquivo das migrations
  - `env.py` - Configuração do Alembic
  - `script.py.mako` - Template para novas migrations

## Criando novas migrations

Se você adicionar novos modelos, execute:

```bash
docker-compose exec app alembic revision --autogenerate -m "Descrição da mudança"
```

Depois confirme as mudanças geradas no arquivo em `alembic/versions/`.

## Variáveis de Ambiente

As variáveis estão configuradas no `docker-compose.yml`:
- `DATABASE_URL`: URL de conexão com PostgreSQL
- `POSTGRES_USER`: user
- `POSTGRES_PASSWORD`: password
- `POSTGRES_DB`: socialapi

Se precisar mudar, edite o `docker-compose.yml` e o `.env` (para desenvolvimento local).

## Troubleshooting

### Erro de conexão ao banco

Certifique-se de que o container do PostgreSQL está saudável:
```bash
docker-compose ps
```

Você deve ver `(healthy)` no serviço `db`.

### Rodar migrations manualmente

```bash
docker-compose exec app alembic upgrade head
```

### Ver logs da aplicação

```bash
docker-compose logs -f app
```

### Ver logs do banco

```bash
docker-compose logs -f db
```
