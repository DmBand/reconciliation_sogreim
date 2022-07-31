from django.db import models


class ProductCategory(models.Model):
    """ Категория товаров """
    name = models.CharField(
        max_length=50,
        verbose_name='название категории',
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория товара'
        verbose_name_plural = 'категории товаров'
        ordering = ['name']


class Product(models.Model):
    """ Товар """
    name = models.CharField(
        max_length=100,
        verbose_name='товар',
        unique=True,
        db_index=True,
    )
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        verbose_name='категория товара',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['name']


class ReconciliationDate(models.Model):
    """ Дата сверки """
    date = models.DateField(
        verbose_name='дата сверки',
        blank=True,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='товар',
        null=True,
    )

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name = 'дата сверки'
        verbose_name_plural = 'даты сверки'
        ordering = ['product']
