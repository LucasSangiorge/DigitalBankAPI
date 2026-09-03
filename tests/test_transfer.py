def criar_conta(client, owner_name, account_number):        
    resposta = client.post("/accounts/", json={
        "owner_name": owner_name,
        "account_number": account_number,
    })
    assert resposta.status_code == 200
    return resposta.json()


def test_transferencia_move_valor_entre_contas(client):     
    conta_a = criar_conta(client, "Conta A", "AAA-001")       
    conta_b = criar_conta(client, "Conta B", "BBB-001")        

    client.post("/transactions/", json={                       
        "account_id": conta_a["id"],
        "type": "deposit",
        "amount": 100,
    })

    resposta = client.post("/transfers/", json={                
        "from_account_id": conta_a["id"],
         "to_account_id": conta_b["id"],                                                    
        "amount": 30,                                            
    })
    assert resposta.status_code == 200                          

    saldo_a = client.get(f"/accounts/{conta_a['id']}").json()["balance"]   
    saldo_b = client.get(f"/accounts/{conta_b['id']}").json()["balance"]   
    assert saldo_a == 70.0                                      
    assert saldo_b == 30.0                                       


def test_transferencia_com_saldo_insuficiente_falha(client):  
    conta_a = criar_conta(client, "Conta A", "AAA-001")         
    conta_b = criar_conta(client, "Conta B", "BBB-001")         

    resposta = client.post("/transfers/", json={                
        "from_account_id": conta_a["id"],
        "to_account_id": conta_b["id"],
        "amount": 9999,                                         
    })

    assert resposta.status_code == 400                          
    saldo_a = client.get(f"/accounts/{conta_a['id']}").json()["balance"]   
    assert saldo_a == 0.0                                     