from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from icecream import ic




class ProductListView(ListView):
    model = Product
    template_name = 'shop/product/list.html'
    context_object_name = 'products'



class ProductDetailView(DetailView):
    model = Product
    template_name ='shop/product/detail.html'
    context_object_name = 'product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ic(self.object.get_product_colors())
        context['product_colors'] = self.object.get_product_colors()
        context['product_sizes'] = self.object.get_product_sizes()
        context['product_reviews'] = self.object.get_product_reviews()
        return context