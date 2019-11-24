from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("dashboard/", views.dashboard),
    path("make_transaction/", views.make_transaction),
    path("make_transaction/confirm", views.confirm_transaction),
]
