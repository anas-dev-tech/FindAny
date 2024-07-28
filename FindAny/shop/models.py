from django.db import models
from taggit.managers import TaggableManager
from colorfield.fields import ColorField
from django.core.exceptions import ValidationError
from icecream import ic




class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = TaggableManager()


    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_final_price(self):
        if self.discount_price:
            return self.discount_price
        return self.price
    
    def clean(self):
        total_variant_quantity = self.variants.aggregate(total=models.Sum('quantity'))['total'] or 0
        if total_variant_quantity != self.stock:
            raise ValidationError('Total variant quantity must match product quantity')


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d')

    def __str__(self):
        return self.product.name

class Color(models.Model):
    COLOR_PALETTE = [
        ("#FFFFFF", "white", ),
        ("#000000", "black", ),
    ]

    # not restrictive, allows the selection of another color from the spectrum.
    color = ColorField(samples=COLOR_PALETTE)
    name = models.CharField(max_length=50)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['color'], name='unique_color'),
            models.UniqueConstraint(fields=['name'], name='unique_name')
        ]
    
    def __str__(self):
        return self.name
    
    
class Size(models.Model):
    size = models.CharField(max_length=200, db_index=True)

    def __str__(self):
        return self.size



class ProductVariant(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='variants'
    )
    
    color = models.ForeignKey(
        Color,
        on_delete=models.CASCADE,
        related_name='products_with_this_color'
    )
    
    size = models.ForeignKey(
        Size,
        on_delete=models.CASCADE,
        related_name='products_with_this_size'
    )
    
    quantity = models.PositiveIntegerField(default=0)
    
    

    
    
    