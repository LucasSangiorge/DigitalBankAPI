const API_URL = "";

function showMessage(elementId, text, isError) {
    const el = document.getElementById(elementId);
    el.textContent = text;
    el.className = "msg " + (isError ? "error" : "success");
}

const accountsTable = new Tabulator("#table-accounts", {
    layout: "fitColumns",
    columns: [
        { title: "ID", field: "id", width: 60 },
        { title: "Titular", field: "owner_name" },
        { title: "Número da conta", field: "account_number" },
        { title: "Saldo", field: "balance" },
    ],
});

const extratoTable = new Tabulator("#table-extrato", {
    layout: "fitColumns",
    columns: [
        { title: "ID", field: "id", width: 60 },
        { title: "Tipo", field: "type" },
        { title: "Valor", field: "amount" },
        { title: "Data", field: "created_at" },
    ],
});

async function loadAccounts() {
    const response = await fetch(`${API_URL}/accounts/`);
    const accounts = await response.json();
    accountsTable.setData(accounts);
}

document.getElementById("btn-refresh-accounts").addEventListener("click", loadAccounts);

document.getElementById("form-account").addEventListener("submit", async (event) => {
    event.preventDefault();
    const owner_name = document.getElementById("owner_name").value;
    const account_number = document.getElementById("account_number").value;

    const response = await fetch(`${API_URL}/accounts/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ owner_name, account_number }),
    });

    if (response.ok) {
        showMessage("msg-account", "Conta criada com sucesso!", false);
        event.target.reset();
        loadAccounts();
    } else {
        const error = await response.json();
        showMessage("msg-account", error.detail || "Erro ao criar conta", true);
    }
});

document.getElementById("form-transaction").addEventListener("submit", async (event) => {
    event.preventDefault();
    const account_id = Number(document.getElementById("tx-account-id").value);
    const type = document.getElementById("tx-type").value;
    const amount = Number(document.getElementById("tx-amount").value);

    const response = await fetch(`${API_URL}/transactions/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ account_id, type, amount }),
    });

    if (response.ok) {
        showMessage("msg-transaction", "Operação realizada com sucesso!", false);
        event.target.reset();
        loadAccounts();
    } else {
        const error = await response.json();
        showMessage("msg-transaction", error.detail || "Erro na operação", true);
    }
});

document.getElementById("form-transfer").addEventListener("submit", async (event) => {
    event.preventDefault();
    const from_account_id = Number(document.getElementById("from-account-id").value);
    const to_account_id = Number(document.getElementById("to-account-id").value);
    const amount = Number(document.getElementById("transfer-amount").value);

    const response = await fetch(`${API_URL}/transfers/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ from_account_id, to_account_id, amount }),
    });

    if (response.ok) {
        showMessage("msg-transfer", "Transferência realizada com sucesso!", false);
        event.target.reset();
        loadAccounts();
    } else {
        const error = await response.json();
        showMessage("msg-transfer", error.detail || "Erro na transferência", true);
    }
});

document.getElementById("form-extrato").addEventListener("submit", async (event) => {
    event.preventDefault();
    const account_id = document.getElementById("extrato-account-id").value;

    const response = await fetch(`${API_URL}/transactions/account/${account_id}`);
    const transactions = await response.json();
    extratoTable.setData(transactions);
});

loadAccounts();
