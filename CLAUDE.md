# DigitalBankAPI

Projeto de estudo, segundo projeto do Lucas depois do [ShopFlowAPI](../ShopFlowAPI) — criado pra reforçar o padrão model→schema→crud→router praticando algo novo: **PostgreSQL** (via Neon, plano gratuito) e **transações atômicas** de banco de dados.

## Contexto

Lucas é estudante de ADS (Estácio, formatura 2026), migrando de carreira da Logística pra Desenvolvimento Backend. Aprendeu o padrão de camadas no ShopFlowAPI (SQLite) digitando o código ele mesmo, com revisão linha a linha. Aqui o objetivo é o mesmo método de trabalho: ele digita, a IA revisa e explica o porquê de cada erro — não escrever o código por ele.

## Domínio: mini banco digital

Simula operações bancárias básicas — contas, transações e transferências entre contas.

## Entidades planejadas

**`Account`** (conta bancária):
- `id`, `owner_name: str`, `account_number: str` (único), `balance: float`

**`Transaction`** (depósito/saque numa única conta):
- `id`, `account_id` (FK), `type: str` (`"deposit"`/`"withdraw"`), `amount: float`, `created_at: datetime`

**`Transfer`** (transferência entre 2 contas — aqui entra o conceito novo de transação atômica):
- `id`, `from_account_id` (FK), `to_account_id` (FK), `amount: float`, `created_at: datetime`

## Decisões técnicas

- **Banco**: PostgreSQL via Neon (nuvem, gratuito, mesmo serviço usado no projeto FluxoMed dele). Connection string fica em `.env` (nunca commitado — já está no `.gitignore`).
- **Conceito central novo**: transferência entre contas precisa ser **atômica** — debitar de uma conta e creditar em outra tem que acontecer como uma coisa só; se der erro no meio, nada é salvo (rollback). Ainda não implementado — é o próximo grande aprendizado desse projeto.
- Reaproveitar todas as convenções já fixadas no ShopFlowAPI (ver `ROADMAP.md` de lá): 4 espaços de indentação, singular/plural em nomes de função, update sempre parcial, `__tablename__` em inglês plural, 404 tratado em toda busca por id.

## Status

Estrutura de pastas criada (`app/models`, `app/schemas`, `app/crud`, `app/routers`), `requirements.txt` e `.gitignore` prontos. Aguardando Lucas criar a conta/banco no Neon e a connection string, antes de começar o `database.py`.
