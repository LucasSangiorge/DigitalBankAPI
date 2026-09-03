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

## Próximo passo planejado (depois do backend pronto)

Frontend simples tipo "sistema de agência bancária" — visualmente básico (sem preocupação de design, igual sistemas reais de banco/triagem que Lucas já viu no dia a dia), só funcional: buscar conta, ver saldo, fazer depósito/saque/transferência. HTML + JS puro consumindo a API via `fetch`, com **Tabulator.js** pra exibir as tabelas (mesma técnica já usada no `agenda-medica-flask`) — decisão confirmada em 2026-09-02, descartada a opção de usar SQLAdmin (painel admin auto-gerado) por ficar menos parecido com uma tela de atendente de verdade. Só entra depois que `Transaction` e `Transfer` (com a transação atômica) estiverem prontos e testados — não interromper o aprendizado de backend pra isso agora.

Depois do frontend: adicionar **testes automatizados (Pytest)** e um **pipeline básico de CI/CD (GitHub Actions)** rodando esses testes a cada push — decisão de 2026-09-03, motivada por gap identificado numa vaga real (pede "noções de testes automatizados" e cita CI/CD como diferencial). Mesmo padrão de testes que o FluxoMed já usa.

## Status

Backend completo: os 3 ciclos (`Account`, `Transaction`, `Transfer`) implementados, testados via curl (depósito, transferência atômica, saldo insuficiente, conta duplicada/inexistente — todos os casos validados) e commitados no GitHub. Próximo passo: frontend simples (Tabulator.js), depois testes automatizados + CI/CD.
