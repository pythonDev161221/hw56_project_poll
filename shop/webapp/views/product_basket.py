from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, RedirectView, ListView, DeleteView

from webapp.forms import OrderForm
from webapp.models import Product, ProductBasket


class AddProductBasketView(View):

    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs.get('pk'))
        if product.balance <= 0:
            return redirect('webapp:product_list_view')
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
        return redirect('webapp:product_list_view')


class AddMultipleProductBasketView(View):
    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs.get('pk'))
        print(type(self.request.GET.get('webapp:product_quantity')))
        product_quantity = int(self.request.GET.get('webapp:product_quantity'))
        if product.balance < product_quantity or product_quantity < 1:
            return redirect('webapp:product_list_view')
        if product.products_basket.values():
            basket = product.products_basket.values()
            id = basket[0].get('id')
            volume = basket[0].get('volume')
            if product.balance > volume:
                ProductBasket.objects.filter(id__exact=id).delete()
                ProductBasket(product=product, volume=volume+product_quantity).save()
        else:
            product_basket = ProductBasket(product=product, volume=product_quantity)
            product_basket.save()
        return redirect('webapp:product_list_view')


class ProductBasketListView(ListView):
    template_name = 'product_basket/product_basket_list_view.html'
    model = ProductBasket

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs = super().get_context_data(object_list=object_list, kwargs=kwargs)
        products = ProductBasket.objects.all()

        summ = []
        a = 0
        for product in products:
            total = product.product.price * product.volume
            a += total
            vol = product.volume
            p_id = product.id
            total = {'p_id': p_id, 'total': total, 'vol': vol}
            summ.append(total)
        kwargs['summ'] = summ
        kwargs['total'] = a
        kwargs['form'] = OrderForm()

        return kwargs


class ProductBasketDeleteView(DeleteView):
    model = ProductBasket

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("webapp:product_basket_list_view")


class ProductBasketOneDeleteView(DeleteView):
    model = ProductBasket

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        print(self.object)
        print(self.object.volume)
        if self.object.volume <= 1:
            return redirect(reverse('webapp:product_basket_delete_view', kwargs=kwargs))
        self.object.volume = self.object.volume - 1
        self.object.save()
        return HttpResponseRedirect(success_url)

    def get_success_url(self):
        return reverse("webapp:product_basket_list_view")

