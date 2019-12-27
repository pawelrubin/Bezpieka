from django.urls import path, include, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("approve_panel", views.approve_panel, name="accept_panel"),
    re_path(r"approve/(?P<transid>\d+)$", views.approve_transaction, name="approve"),
    path("make_transaction/", views.make_transaction),
    path("make_transaction/confirm", views.confirm_transaction),
]
