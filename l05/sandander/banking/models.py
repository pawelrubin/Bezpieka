from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

from pprint import pprint


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Transaction(models.Model):
    sender = models.ForeignKey(
        Account, on_delete=models.DO_NOTHING, related_name="sender"
    )
    recipient = models.ForeignKey(
        Account, on_delete=models.DO_NOTHING, related_name="recipient"
    )
    amount = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    title = models.TextField(default="Sandander money transaction.")
    approved = models.BooleanField(default=False)
    executed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.pk and self.executed:
            print(self.__dict__)
            # raise ValidationError(
            #     ("You cannot change existing transaction!!!"),
            #     code="immutable_transaction",
            # )
        super(Transaction, self).save(*args, **kwargs)


@receiver(post_save, sender=Transaction, dispatch_uid="update_accounts_balance")
def update_accounts_balance(sender, instance, created, **kwargs):
    if instance.approved and not instance.executed:
        instance.sender.balance -= instance.amount
        instance.sender.save()
        instance.recipient.balance += instance.amount
        instance.recipient.save()
        instance.executed = True
        instance.save()


@receiver(post_save, sender=User, dispatch_uid="create_account_for_user")
def create_account_for_user(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)
