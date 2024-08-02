from django.contrib import admin
from .models import Review




@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'updated_at')
    list_filter = ('user', 'product')
    




