from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product




class ProductListView(ListView):
    model = Product
    template_name = 'shop/product/list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name ='shop/product/detail.html'
    context_object_name = 'product'