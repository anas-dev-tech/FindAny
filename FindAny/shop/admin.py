from django.contrib import admin
from .models import Product, Category, ProductImage, ProductVariant, Color, Size
from django.contrib import admin

class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1  # Add one empty variant by default



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('category',)
    inlines = [ProductVariantInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    '''Admin View for ProductImage'''

    list_display = ('product', 'image',)
    list_filter = ('product',)

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('color', 'name')


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('size',)
