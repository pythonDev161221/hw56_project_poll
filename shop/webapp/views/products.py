from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from webapp.forms import ProductForm
from webapp.models import Product


class ProductListView(ListView):
    template_name = 'products/product_list_view.html'
    model = Product
    context_object_name = 'products'


class ProductDetailView(DetailView):
    template_name = 'products/product_detail_view.html'
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_create_view.html'
    # success_url = reverse_lazy('product_list_view')

