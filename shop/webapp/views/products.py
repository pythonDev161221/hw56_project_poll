from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm, SearchForm
from webapp.models import Product
from webapp.views.base import SearchView


class ProductListView(SearchView):
    template_name = 'products/product_list_view.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 5
    paginate_orphans = 1
    search_fields = ["product__icontains", "description__icontains"]

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(balance__gt=0).order_by('category', 'product')
        return queryset

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     kwargs = super().get_context_data(**kwargs)
    #     form = SearchForm()
    #     kwargs['form'] = form
    #     print(kwargs)
    #     # if self.kwargs.get('search'):
    #
    #     return kwargs



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
