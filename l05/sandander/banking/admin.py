from django.contrib import admin

from .models import Transaction, Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "balance",
    )


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("sender", "recipient", "amount", "date", "title", "approved", "executed")
