# Generated by Django 2.2.4 on 2020-04-18 11:47

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0003_auto_20200418_1142'),
        ('clients', '0003_auto_20200418_1142'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_sap_id', models.IntegerField(unique=True, validators=[django.core.validators.RegexValidator(code='invalid sap id', message='Numer SAP powinien składać się z dokładnie 6 cyfr', regex='^([0-9]{6})$')])),
                ('date_of_production', models.DateField(default=datetime.date.today)),
                ('status', models.CharField(choices=[('Started', 'Rozpoczęty'), ('Ready', 'Gotowy do pomiarów'), ('Open', 'W trakcie'), ('Done', 'Zakończony')], default='Started', max_length=30)),
                ('quantity', models.IntegerField(validators=[django.core.validators.RegexValidator(message='Pole integer powinno zawierać liczbę całkowitą', regex='^[0-9]*$')])),
                ('internal_diameter_reference', models.FloatField(validators=[django.core.validators.RegexValidator(message='Pole float powinno zawierać liczbę całkowitą bądź zmiennoprzecinkową', regex='^([0-9]*|[0-9]*\\.\\d+)$')])),
                ('external_diameter_reference', models.FloatField(validators=[django.core.validators.RegexValidator(message='Pole float powinno zawierać liczbę całkowitą bądź zmiennoprzecinkową', regex='^([0-9]*|[0-9]*\\.\\d+)$')])),
                ('length', models.FloatField(validators=[django.core.validators.RegexValidator(message='Pole float powinno zawierać liczbę całkowitą bądź zmiennoprzecinkową', regex='^([0-9]*|[0-9]*\\.\\d+)$')])),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='clients.Client')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='MeasurementReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('date_of_control', models.DateField(default=datetime.date.today)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='measurement_report', to='orders.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pallet_number', models.IntegerField(validators=[django.core.validators.RegexValidator(message='Pole integer powinno zawierać liczbę całkowitą', regex='^[0-9]*$')])),
                ('internal_diameter_tolerance_top', models.FloatField(validators=[django.core.validators.RegexValidator(message='Pole float powinno zawierać liczbę całkowitą bądź zmiennoprzecinkową', regex='^([0-9]*|[0-9]*\\.\\d+)$')])),
                ('internal_diameter_target', models.FloatField(validators=[django.core.validators.RegexValidator(message='Pole float powinno zawierać liczbę całkowitą bądź zmiennoprzecinkową', regex='^([0-9]*|[0-9]*\\.\\d+)$')])),
                ('internal_diameter_tolerance_bottom', models.FloatField(validators=[django.core.validators.RegexValidator(message='Pole float powinno zawierać liczbę całkowitą bądź zmiennoprzecinkową', regex='^([0-9]*|[0-9]*\\.\\d+)$')])),
                ('external_diameter_tolerance_top', models.FloatField(validators=[django.core.validators.RegexValidator(message='Pole float powinno zawierać liczbę całkowitą bądź zmiennoprzecinkową', regex='^([0-9]*|[0-9]*\\.\\d+)$')])),
                ('external_diameter_target', models.FloatField(validators=[django.core.validators.RegexValidator(message='Pole float powinno zawierać liczbę całkowitą bądź zmiennoprzecinkową', regex='^([0-9]*|[0-9]*\\.\\d+)$')])),
                ('external_diameter_tolerance_bottom', models.FloatField(validators=[django.core.validators.RegexValidator(message='Pole float powinno zawierać liczbę całkowitą bądź zmiennoprzecinkową', regex='^([0-9]*|[0-9]*\\.\\d+)$')])),
                ('length_tolerance_top', models.FloatField(validators=[django.core.validators.RegexValidator(message='Pole float powinno zawierać liczbę całkowitą bądź zmiennoprzecinkową', regex='^([0-9]*|[0-9]*\\.\\d+)$')])),
                ('length_target', models.FloatField(validators=[django.core.validators.RegexValidator(message='Pole float powinno zawierać liczbę całkowitą bądź zmiennoprzecinkową', regex='^([0-9]*|[0-9]*\\.\\d+)$')])),
                ('length_tolerance_bottom', models.FloatField(validators=[django.core.validators.RegexValidator(message='Pole float powinno zawierać liczbę całkowitą bądź zmiennoprzecinkową', regex='^([0-9]*|[0-9]*\\.\\d+)$')])),
                ('flat_crush_resistance_target', models.IntegerField(validators=[django.core.validators.RegexValidator(message='Pole integer powinno zawierać liczbę całkowitą', regex='^[0-9]*$')])),
                ('moisture_content_target', models.IntegerField(validators=[django.core.validators.RegexValidator(message='Pole integer powinno zawierać liczbę całkowitą', regex='^[0-9]*$')])),
                ('weight', models.IntegerField(validators=[django.core.validators.RegexValidator(message='Pole integer powinno zawierać liczbę całkowitą', regex='^[0-9]*$')])),
                ('remarks', models.TextField()),
                ('measurement_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='orders.MeasurementReport')),
            ],
        ),
    ]