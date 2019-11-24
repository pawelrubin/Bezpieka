from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User

from .forms import SignUpForm, TransactionForm
from .models import Transaction


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def index(request: WSGIRequest):
    if request.user.is_authenticated:
        return render(request, "index.html")
    return redirect("/accounts/login")


def dashboard(request: WSGIRequest):
    if request.user.is_authenticated:
        return render(
            request,
            "dashboard.html",
            context={
                "transactions": {
                    "send": Transaction.objects.filter(
                        sender__user__username=request.user.username
                    ),
                    "received": Transaction.objects.filter(
                        recipient__user__username=request.user.username
                    ),
                }
            },
        )
    return redirect("/accounts/login")


def make_transaction(request: WSGIRequest):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = TransactionForm(request.POST)
            if form.is_valid():
                return render(
                    request,
                    "confirm_transaction.html",
                    {"transaction": form.cleaned_data},
                )
        else:
            form = TransactionForm()
        return render(request, "make_transaction.html", {"form": form})
    return redirect("/accounts/login")


def confirm_transaction(request: WSGIRequest):
    if request.user.is_authenticated and request.method == "POST":
        Transaction.objects.create(
            sender=request.user.account,
            recipient=User.objects.get(username=request.POST["recipient"]).account,
            amount=int(request.POST["amount"]),
        )
        return render(
            request,
            "transaction_completed.html",
            context={
                "recipient": request.POST["recipient"],
                "amount": request.POST["amount"],
            },
        )
    return redirect("/accounts/login")
