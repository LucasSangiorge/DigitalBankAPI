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

## Decisões de frontend e testes (histórico)

Frontend simples tipo "sistema de agência bancária" — visualmente básico, só funcional: buscar conta, ver saldo, fazer depósito/saque/transferência. HTML + JS puro consumindo a API via `fetch`, com **Tabulator.js** pra exibir as tabelas (mesma técnica já usada no `agenda-medica-flask`) — decisão confirmada em 2026-09-02, descartada a opção de usar SQLAdmin (painel admin auto-gerado) por ficar menos parecido com uma tela de atendente de verdade.

Testes automatizados (Pytest) + CI/CD (GitHub Actions) — decisão de 2026-09-03, motivada por gap identificado numa vaga real (pede "noções de testes automatizados" e cita CI/CD como diferencial). Mesmo padrão de testes que o FluxoMed já usa (`conftest.py` com banco SQLite em memória via `dependency_overrides`, sem tocar no Neon de produção). Pegadinha resolvida: `app/main.py` roda `Base.metadata.create_all(bind=engine)` no import, usando o `DATABASE_URL` real — no GitHub Actions isso quebraria (sem `.env`), resolvido setando um `DATABASE_URL` fake (`sqlite:///./ci.db`) como variável de ambiente do workflow.

## Status — projeto concluído (2026-09-03)

Roadmap completo: backend (`Account`, `Transaction`, `Transfer` com transação atômica) → frontend simples (Tabulator.js) → 7 testes automatizados (Pytest) cobrindo os 3 ciclos e os casos de erro → pipeline de CI/CD no GitHub Actions rodando os testes a cada push (primeira execução: sucesso, 20s). Tudo commitado e no ar em `github.com/LucasSangiorge/DigitalBankAPI`.

Possíveis próximos passos, sem urgência: entidade `Customer` (1:N com `Account`, discutido mas não decidido), Alembic para migrations, deploy do backend + frontend na nuvem.
