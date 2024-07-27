from django.contrib import admin
from .models import Product, Category, ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('category',)
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    '''Admin View for ProductImage'''

    list_display = ('product', 'image',)
    list_filter = ('product',)
   