# Generated by Django 2.2.10 on 2020-09-18 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200718_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Started', 'Otwarty'), ('Open', 'W trakcie'), ('Done', 'Zakończony')], default='Started', max_length=30),
        ),
    ]