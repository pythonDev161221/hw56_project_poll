from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, RedirectView

from webapp.models import Product, ProductBasket


class AddProductView(View):

    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs.get('pk'))
        if product.balance <= 0:
            return redirect('product_list_view')
        if product.products_basket.values():
            basket = product.products_basket.values()
            id = basket[0].get('id')
            volume = basket[0].get('volume')
            if product.balance > volume:
                ProductBasket.objects.filter(id__exact=id).delete()
                ProductBasket(product=product, volume=volume+1).save()
        else:
            product_basket = ProductBasket(product=product, volume=1)
            product_basket.save()
        return redirect('product_list_view')

