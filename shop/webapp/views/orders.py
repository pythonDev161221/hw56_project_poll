from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import OrderForm
from webapp.models import ProductBasket, Order, OrderProduct


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm

    def form_valid(self, form):
        basket_session = self.request.session.get('product_basket')
        pk_session = self.request.session.get('pk')
        products_basket = ProductBasket.objects.filter(
            pk__in=basket_session, session__exact=pk_session
        )

        for product_basket in products_basket:
            if product_basket.product.balance < product_basket.volume:
                raise ValueError(
                    f'В магазине нет столько товара. Вы хотите {product_basket.volume}'
                    f' а в наличии только {product_basket.product.balance}')
        order = form.save()
        try:
            order.user = self.request.user
        except:
            pass
        order.save()
        for product_basket in products_basket:
            order_product = OrderProduct.objects.create(product=product_basket.product,
                                                        volume=product_basket.volume,
                                                        order=order)
            order_product.save()
            product_basket.product.balance -= product_basket.volume
            product_basket.product.save()

        ProductBasket.objects.filter(pk__in=basket_session, session__exact=pk_session).delete()
        self.request.session['product_basket'] = []
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:product_basket_list_view')
