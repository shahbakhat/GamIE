from django.contrib import admin
from . models import Product,Category
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    """
    Custom admin Product Model.
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Custom admin Category Model
    """
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)