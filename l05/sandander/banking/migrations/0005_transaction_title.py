# Generated by Django 3.0 on 2019-12-28 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0004_transaction_executed'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='title',
            field=models.TextField(default=''),
        ),
    ]