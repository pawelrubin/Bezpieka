# Generated by Django 3.0 on 2019-12-27 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("banking", "0002_transaction_aprooved"),
    ]

    operations = [
        migrations.RenameField(
            model_name="transaction", old_name="aprooved", new_name="approved",
        ),
    ]
