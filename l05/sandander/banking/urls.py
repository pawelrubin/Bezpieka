from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", views.SignUpView.as_view(), name="signup"),
]
