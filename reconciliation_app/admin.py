from django.contrib import admin
from .models import ProductCategory, Product, ReconcilicationDate


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name',)
    list_filter = ('category',)


class ReconcilicationDateAdmin(admin.ModelAdmin):
    list_display = ('date', 'product')


admin.site.register(ProductCategory)
admin.site.register(Product, ProductAdmin)
admin.site.register(ReconcilicationDate, ReconcilicationDateAdmin)
