from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def index(request: WSGIRequest):
    if request.user.is_authenticated:
        return render(request, "index.html")
    return redirect("/accounts/login")
