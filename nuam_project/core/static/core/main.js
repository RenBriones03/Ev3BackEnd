// ====== Conversor ======
async function convertCurrency() {
  const amount = document.getElementById('amount').value;
  const from = document.getElementById('from').value;
  const to = document.getElementById('to').value;
  const result = document.getElementById('result');

  try {
    const res = await fetch(`/api/exchange-rates/convert/?amount=${amount}&from=${from}&to=${to}`);
    const data = await res.json();
    if (res.ok) {
      result.textContent = `${data.converted_amount} ${to}`;
    } else {
      result.textContent = `Error: ${data.detail}`;
    }
  } catch (err) {
    result.textContent = 'Error de conexión con el servidor';
  }
}

// ====== CRUD Transacciones ======
async function loadTransactions() {
  const res = await fetch('/api/transactions/');
  const data = await res.json();
  const tbody = document.querySelector('#txTable tbody');
  tbody.innerHTML = '';
  data.forEach(tx => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>${tx.id}</td>
      <td>${tx.description}</td>
      <td>${tx.amount}</td>
      <td>${tx.currency}</td>
      <td>${tx.location}</td>
      <td>${tx.amount_in_usd || '-'}</td>
      <td><button onclick="deleteTransaction(${tx.id})">🗑️</button></td>
    `;
    tbody.appendChild(tr);
  });
}

async function createTransaction(e) {
  e.preventDefault();
  const tx = {
    description: document.getElementById('desc').value,
    amount: document.getElementById('amountTx').value,
    currency: document.getElementById('currencyTx').value,
    location: document.getElementById('locationTx').value,
  };
  const res = await fetch('/api/transactions/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(tx)
  });
  if (res.ok) {
    document.getElementById('txForm').reset();
    loadTransactions();
  } else {
    alert('Error al crear transacción');
  }
}

async function deleteTransaction(id) {
  if (!confirm('¿Eliminar transacción?')) return;
  await fetch(`/api/transactions/${id}/`, { method: 'DELETE' });
  loadTransactions();
}

document.addEventListener('DOMContentLoaded', () => {
  if (window.location.pathname.includes('transactions')) {
    loadTransactions();
  }
});
