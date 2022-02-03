from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from webapp.models import Product


class ProductListView(ListView):
    template_name = 'products/product_list_view.html'
    model = Product
    context_object_name = 'products'
