from django.contrib import admin
from .models import ProductCategory, Product, ReconciliationDate


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name',)
    list_filter = ('category',)


class ReconcilicationDateAdmin(admin.ModelAdmin):
    list_display = ('date', 'product')
    list_filter = ('product',)
    ordering = ['date']


admin.site.register(ProductCategory)
admin.site.register(Product, ProductAdmin)
admin.site.register(ReconciliationDate, ReconcilicationDateAdmin)
