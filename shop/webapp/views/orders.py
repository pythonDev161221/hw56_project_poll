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
        product_basket = ProductBasket.objects.filter(pk__in=basket_session)

        for product_basket_one in product_basket:
            if product_basket_one.product.balance < product_basket_one.volume:
                raise ValueError(
                    f'В магазине нет столько товара. Вы хотите {product_basket_one.volume}'
                    f' а в наличии только {product_basket_one.product.balance}')
        order = form.save()
        order.user = self.request.user
        order.save()
        for product_basket_one in product_basket:
            order_product = OrderProduct.objects.create(product=product_basket_one.product,
                                                        volume=product_basket_one.volume,
                                                        order=order)
            order_product.save()
            product_basket_one.product.balance -= product_basket_one.volume
            product_basket_one.product.save()

        ProductBasket.objects.filter(pk__in=basket_session).delete()
        self.request.session['product_basket'] = []
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:product_basket_list_view')
