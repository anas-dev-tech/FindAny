from django.db import models
from django.contrib.auth import get_user_model
from shop.models import Product
User = get_user_model()




class Review(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    
    content = models.CharField(
        max_length=500
    )
    
    create_at = models.DateTimeField(
        auto_now_add=True
    )
    
    updated_at = models.DateTimeField(
        auto_now=True
    )
    
    
    
    
    def __str__(self):
        return f'{self.user} at {self.updated_at}'