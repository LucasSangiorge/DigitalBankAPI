def criar_conta(client, owner_name, account_number):
    resposta = client.post("/accounts/", json={
        "owner_name": owner_name,
        "account_number": account_number,
    })
    assert resposta.status_code == 200
    return resposta.json()

def test_criar_conta_comeca_com_saldo_zero(client):
    conta = criar_conta(client, "Conta A", "AAA-001")
    assert conta["balance"] == 0.0

def test_buscar_conta_inexistente_retorna_404(client):
    resposta = client.get("/accounts/9999")
    assert resposta.status_code == 404    