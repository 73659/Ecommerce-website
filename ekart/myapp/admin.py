from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'cat', 'product_details', 'is_active', 'p_img']
    list_filter = ['cat', 'is_active']
# Register your models here.
admin.site.register(Product, ProductAdmin)