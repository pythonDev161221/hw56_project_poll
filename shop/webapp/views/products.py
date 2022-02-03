from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm
from webapp.models import Product


class ProductListView(ListView):
    template_name = 'products/product_list_view.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 5
    paginate_orphans = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(balance__gt=0).order_by('category', 'product')
        return queryset



class ProductDetailView(DetailView):
    template_name = 'products/product_detail_view.html'
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_create_view.html'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_update_view.html'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_delete_view.html'
    success_url = reverse_lazy('product_list_view')
