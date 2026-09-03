def criar_conta(client, owner_name, account_number):
    resposta = client.post("/accounts/", json={
        "owner_name": owner_name,
        "account_number": account_number,
    })
    assert resposta.status_code == 200
    return resposta.json()

def test_deposito_aumentado(client):
    conta = criar_conta(client, "Conta A", "AAA-001")

    resposta = client.post("/transactions/", json={
        "account_id": conta["id"],
        "type": "deposit",
        "amount": 100,
    })
    assert resposta.status_code ==200

    conta_atualizada = client.get(f"/accounts/{conta['id']}").json()
    assert conta_atualizada["balance"] == 100.0


def test_saque_maior_que_saldo_retorna_400(client):
    conta = criar_conta(client, "Conta B", "BBB-001")

    resposta = client.post("/transactions/", json={
        "account_id": conta["id"],
        "type": "withdraw",
        "amount": 100,
    })
    assert resposta.status_code == 400

def test_transacao_em_conta_inexistente_retorna_404(client):
    resposta = client.post("/transactions/", json={
        "account_id": 9999,
        "type": "deposit",
        "amount": 100,
    })
    assert resposta.status_code == 404