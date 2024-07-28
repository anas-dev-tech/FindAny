from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ProductVariant
from django.db import models
from icecream import ic

@receiver(post_save, sender=ProductVariant)
def update_product_quantity(sender, 
                            instance, created, **kwargs):
    product = instance.product
    total_variant_quantity = product.variants.aggregate(total=models.Sum('quantity'))['total'] or 0
    ic(total_variant_quantity)
    product.stock = total_variant_quantity
    product.save()
