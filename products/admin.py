from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Category)


# Changing admin panel view to upload ProductImages with Product
class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]


admin.site.register(Product, ProductAdmin)