from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='название категории', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория товара'
        verbose_name_plural = 'категории товаров'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='товар', unique=True, db_index=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, verbose_name='категория товара')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['category']
