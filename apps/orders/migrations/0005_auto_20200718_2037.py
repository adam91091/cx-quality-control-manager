# Generated by Django 2.2.10 on 2020-07-18 18:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20200419_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_sap_id',
            field=models.IntegerField(blank=True, null=True, unique=True, validators=[django.core.validators.RegexValidator(code='invalid sap id', message='Numer SAP powinien składać się z dokładnie 6 cyfr', regex='^([0-9]{6})$')]),
        ),
    ]
