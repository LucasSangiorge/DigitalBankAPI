# DigitalBankAPI

API REST de um mini banco digital construída em Python com **FastAPI** e **SQLAlchemy**, seguindo uma arquitetura em camadas (model → schema → CRUD → router).

Projeto de estudo com foco em **PostgreSQL na nuvem** e **transações atômicas de banco de dados** — o conceito por trás de qualquer transferência bancária real: debitar de uma conta e creditar em outra precisa acontecer como uma única operação. Se algo der errado no meio do caminho, nada é salvo.

🔗 **Demo ao vivo:** [digitalbankapi.onrender.com](https://digitalbankapi.onrender.com)
📄 **Documentação da API:** [digitalbankapi.onrender.com/docs](https://digitalbankapi.onrender.com/docs)

> Serviço hospedado no plano gratuito do Render — pode levar até ~50 segundos pra "acordar" na primeira requisição depois de um tempo sem uso.

## Stack

- **Python**
- **FastAPI** — framework web assíncrono, com documentação automática (Swagger/OpenAPI)
- **SQLAlchemy** — ORM para modelagem e acesso ao banco de dados
- **Pydantic** — validação e serialização de dados
- **PostgreSQL** (via Neon) — banco de dados na nuvem
- **Pytest** — testes automatizados
- **GitHub Actions** — pipeline de CI, rodando os testes a cada push
- **Render** — deploy contínuo (CD), publicado automaticamente a cada push na branch `main`
- **HTML/CSS/JS + Tabulator.js** — frontend simples consumindo a API

## Funcionalidades

- **3 entidades**: `Account`, `Transaction` (depósito/saque) e `Transfer` (transferência entre contas)
- **Transação atômica real** no `Transfer` — validação de saldo insuficiente, conta inexistente e transferência para a mesma conta, tudo antes de qualquer alteração no banco
- **7 testes automatizados** (Pytest) cobrindo os casos de sucesso e de erro das 3 entidades
- **Frontend simples** tipo "sistema de agência bancária" — criar conta, depósito/saque, transferência e extrato

## ⚠️ Limitação conhecida — sem autenticação

Este projeto **não implementa autenticação**. O foco de aprendizado aqui foi transação atômica e não segurança de acesso — qualquer pessoa com o link consegue criar, alterar ou remover contas e transações reais no banco. É um projeto de estudo com dados fictícios, sem informação sensível, então o risco é baixo (a demo pode ficar "bagunçada" se alguém mexer, nada além disso). Autenticação é um próximo passo natural do roadmap.

## Estrutura do projeto

```
app/
├── models/      # Tabelas do banco (SQLAlchemy)
├── schemas/     # Contratos de entrada/saída da API (Pydantic)
├── crud/        # Regras de acesso e manipulação de dados
├── routers/     # Endpoints REST (FastAPI)
├── database.py  # Configuração de conexão com o banco
└── main.py      # Ponto de entrada da aplicação
frontend/        # HTML/CSS/JS consumindo a API
tests/           # Testes automatizados (Pytest)
.github/workflows/  # Pipeline de CI (GitHub Actions)
```

## Como rodar localmente

```bash
git clone https://github.com/LucasSangiorge/DigitalBankAPI.git
cd DigitalBankAPI
python -m venv venv
source venv/Scripts/activate       # Windows (Git Bash)
pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz com sua connection string do PostgreSQL:
```
DATABASE_URL=postgresql://usuario:senha@host/banco?sslmode=require
```

```bash
uvicorn app.main:app --reload
```

Acesse `http://127.0.0.1:8000` (frontend) ou `http://127.0.0.1:8000/docs` (documentação interativa).

## Como rodar os testes

```bash
python -m pytest tests/ -v
```

## Endpoints principais

| Recurso | Rotas |
|---|---|
| Contas | `POST /accounts/`, `GET /accounts/`, `GET /accounts/{id}`, `PUT /accounts/{id}`, `DELETE /accounts/{id}` |
| Transações | `POST /transactions/`, `GET /transactions/{id}`, `GET /transactions/account/{account_id}` |
| Transferências | `POST /transfers/`, `GET /transfers/{id}` |
