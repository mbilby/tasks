# Tasks API

API REST em FastAPI para gerenciamento de atividades, com PostgreSQL, SQLAlchemy e Alembic.

## O que existe aqui

- CRUD de atividades.
- Banco PostgreSQL com nome `Tasks`.
- Migração inicial pronta para criar a tabela `activities`.
- Documentação da API em `/docs`.
- Apresentação do sistema em `docs/apresentacao.md`.

## Campos da atividade

- `id`: hash gerado automaticamente.
- `titulo`
- `agente_responsavel`
- `data_inicio`
- `data_conclusao`
- `descricao`
- `status`

## Requisitos

- Python 3.12+
- Docker e Docker Compose, se quiser subir tudo de uma vez.
- PostgreSQL, se for rodar fora do Docker.

## Estrutura

```text
tasks-api/
├── app/
├── alembic/
├── docs/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

## Como rodar com Docker

1. Copie o arquivo de ambiente:

```bash
cp .env.example .env
```

2. Suba a aplicação e o banco:

```bash
docker compose up --build
```

3. Rode as migrações se o container da API não fizer isso automaticamente:

```bash
docker compose exec api alembic upgrade head
```

4. Acesse:

- API: `http://localhost:8000`
- Swagger: `http://localhost:8000/docs`
- Healthcheck: `http://localhost:8000/api/v1/health`

## Como rodar localmente

Se preferir rodar sem Docker:

1. Crie e ative um ambiente virtual.
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Configure o banco PostgreSQL e ajuste `DATABASE_URL` no `.env`.

4. Aplique as migrações:

```bash
alembic upgrade head
```

5. Inicie a API:

```bash
uvicorn app.main:app --reload
```

## Variáveis de ambiente

| Variável | Valor padrão | Descrição |
| --- | --- | --- |
| `DATABASE_URL` | `postgresql+psycopg://tasks:tasks@localhost:5432/Tasks` | Conexão com o PostgreSQL |
| `APP_NAME` | `Tasks API` | Nome exibido pela aplicação |
| `API_PREFIX` | `/api/v1` | Prefixo das rotas |

## Rotas

| Método | Rota | Descrição |
| --- | --- | --- |
| `POST` | `/api/v1/activities` | Cria uma atividade |
| `GET` | `/api/v1/activities` | Lista atividades |
| `GET` | `/api/v1/activities/{activity_id}` | Busca uma atividade |
| `PATCH` | `/api/v1/activities/{activity_id}` | Atualiza uma atividade |
| `DELETE` | `/api/v1/activities/{activity_id}` | Remove uma atividade |

## Exemplo de criação

```bash
curl -X POST http://localhost:8000/api/v1/activities \
  -H "Content-Type: application/json" \
  -d '{
    "titulo": "Revisar backlog",
    "agente_responsavel": "Marcelo",
    "data_inicio": "2026-07-01",
    "descricao": "Separar as atividades da sprint",
    "status": "pendente"
  }'
```

## Exemplo de atualização

```bash
curl -X PATCH http://localhost:8000/api/v1/activities/{activity_id} \
  -H "Content-Type: application/json" \
  -d '{
    "status": "concluida",
    "data_conclusao": "2026-07-01"
  }'
```

## Banco de dados

O projeto usa o banco `Tasks` e a tabela `activities`, criada pela migration inicial em:

```text
alembic/versions/0001_create_activities_table.py
```

## Observações

- O `id` da atividade é um hash SHA-256 gerado no backend.
- Se a atividade for criada como `concluida` sem `data_conclusao`, a API preenche com a data atual.
- A API expõe documentação automática no Swagger.
