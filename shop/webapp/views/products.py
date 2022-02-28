from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView


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


class ProductDetailView(DetailView):
    template_name = 'products/product_detail_view.html'
    model = Product


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_create_view.html'
    permission_required = 'webapp.add_product'


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_update_view.html'
    permission_required = 'webapp.change_product'


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/product_delete_view.html'
    success_url = reverse_lazy('webapp:product_list_view')
    permission_required = 'webapp.delete_product'
