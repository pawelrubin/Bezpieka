# Generated by Django 3.0 on 2019-12-28 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0005_transaction_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='title',
            field=models.TextField(default='Sandander money transaction.'),
        ),
    ]
