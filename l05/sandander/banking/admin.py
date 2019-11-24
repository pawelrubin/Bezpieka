from django.contrib import admin

from . import models


class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "balance",
    )


class TransactionAdmin(admin.ModelAdmin):
    list_display = ("sender", "recipient", "amount", "date")


admin.site.register(models.Account, AccountAdmin)
admin.site.register(models.Transaction, TransactionAdmin)
