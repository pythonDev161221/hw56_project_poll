from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, RedirectView, ListView, DeleteView

from webapp.models import Product, ProductBasket


class AddProductBasketView(View):

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


class ProductBasketListView(ListView):
    template_name = 'product_basket/product_basket_list_view.html'
    model = ProductBasket

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs = super().get_context_data(object_list=object_list, kwargs=kwargs)
        products = ProductBasket.objects.all()
        summ = []
        for product in products:
            total = product.product.price * product.volume
            p_id = product.id
            total = {'p_id': p_id, 'total': total}
            summ.append(total)
        kwargs['summ'] = summ

        return kwargs


class ProductBasketDeleteView(DeleteView):
    model = ProductBasket

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("product_basket_list_view")

