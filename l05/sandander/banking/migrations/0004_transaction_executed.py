# Generated by Django 3.0 on 2019-12-27 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("banking", "0003_auto_20191227_1426"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="executed",
            field=models.BooleanField(default=False),
        ),
    ]
