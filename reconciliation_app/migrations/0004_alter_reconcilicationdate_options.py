# Generated by Django 4.0.5 on 2022-06-11 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reconciliation_app', '0003_reconcilicationdate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reconcilicationdate',
            options={'ordering': ['product'], 'verbose_name': 'дата сверки', 'verbose_name_plural': 'даты сверки'},
        ),
    ]
