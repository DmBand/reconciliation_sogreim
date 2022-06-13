# Generated by Django 4.0.5 on 2022-06-11 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reconciliation_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['category'], 'verbose_name': 'товар', 'verbose_name_plural': 'товары'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'ordering': ['name'], 'verbose_name': 'категория товара', 'verbose_name_plural': 'категории товаров'},
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(db_index=True, max_length=100, unique=True, verbose_name='товар'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='название категории'),
        ),
    ]
