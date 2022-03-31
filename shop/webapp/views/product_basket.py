from uuid import uuid4

from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, RedirectView, ListView, DeleteView

from webapp.forms import OrderForm
from webapp.models import Product, ProductBasket
User = get_user_model()

class AddProductBasketView(View):

    def get(self, request, *args, **kwargs):
        basket_session = request.session.get('product_basket', [])
        pk_session = request.session.get('pk', uuid4().hex)
        request.session['pk'] = pk_session
        product = get_object_or_404(Product, pk=kwargs.get('pk'))
        if product.balance <= 0:
            return redirect('webapp:product_list_view')
        products_basket = ProductBasket.objects.filter(session__exact=pk_session).filter(
            pk__in=basket_session)
        bool_products_in_basket = False
        for product_basket in products_basket:
            if product_basket.product == product:
                bool_products_in_basket = True
                product_basket.volume += 1
                product_basket.save()
            basket_session.append(product_basket.pk)
        if not bool_products_in_basket:
            product_basket = ProductBasket.objects.create(product=product, volume=1, session=pk_session)
            basket_session.append(product_basket.pk)
        request.session['product_basket'] = basket_session
        return redirect('webapp:product_list_view')


        # if product.products_basket.values():
        #     basket = product.products_basket.values()
        #     id = basket[0].get('id')
        #     volume = basket[0].get('volume')
        #     if product.balance > volume:
        #         # ProductBasket.objects.filter(id__exact=id).delete()
        #         # product_basket = ProductBasket.objects.create(product=product, volume=volume+1)
        #         product_basket = ProductBasket.objects.get(id=id)
        #         product_basket.volume += 1
        #         product_basket.save()
        #         basket_session.append(product_basket.pk)
        #         request.session['product_basket'] = basket_session
        # else:
        #     product_basket = ProductBasket.objects.create(product=product, volume=1)
        #     basket_session.append(product_basket.pk)
        #     request.session['product_basket'] = basket_session
        # return redirect('webapp:product_list_view')


class AddMultipleProductBasketView(View):
    def get(self, request, *args, **kwargs):
        pk_session = request.session.get('pk', uuid4().hex)
        request.session['pk'] = pk_session

        basket_session = request.session.get('product_basket', [])
        product = get_object_or_404(Product, pk=kwargs.get('pk'))
        product_quantity = int(self.request.GET.get('product_quantity'))

        if product.balance < product_quantity or product_quantity < 1:
            return redirect('webapp:product_list_view')

        products_basket = ProductBasket.objects.filter(
            session__exact=pk_session, pk__in=basket_session)

        bool_product_in_basket = False
        for product_basket in products_basket:
            if product_basket.product == product:
                bool_product_in_basket = True
                product_basket.volume += product_quantity
                product_basket.save()
            basket_session.append(product_basket.pk)
        if not bool_product_in_basket:
            print("not")
            product_basket = ProductBasket.objects.create(
                product=product, volume=product_quantity, session=pk_session
            )
            basket_session.append(product_basket.pk)
        return redirect('webapp:product_list_view')


class ProductBasketListView(ListView):
    template_name = 'product_basket/product_basket_list_view.html'
    model = ProductBasket

    def get_context_data(self, *, object_list=None, **kwargs):
        pk_session = self.request.session.get('pk', uuid4().hex)
        self.request.session['pk'] = pk_session
        kwargs = super().get_context_data(object_list=object_list,
                                          kwargs=kwargs)

        basket_session = self.request.session.get('product_basket', [])
        products = ProductBasket.objects.filter(session__exact=pk_session, pk__in=basket_session)

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
        kwargs['productbasket_list'] = products

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
        if self.object.volume <= 1:
            return redirect(reverse('webapp:product_basket_delete_view', kwargs=kwargs))
        self.object.volume = self.object.volume - 1
        self.object.save()
        return HttpResponseRedirect(success_url)

    def get_success_url(self):
        return reverse("webapp:product_basket_list_view")
