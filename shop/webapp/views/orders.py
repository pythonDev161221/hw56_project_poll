from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView

from webapp.forms import OrderForm
from webapp.models import Product, ProductBasket, Order, OrderProduct


# class OrderCreateView(View):
#     def post(self, request, *args, **kwargs):
#         product_basket = self.request.POST.get('productbasket_list')
#         if product_basket == '<QuerySet []>':
#             return redirect('product_basket_list_view')
#         product_basket = product_basket.split('[')[1]
#         product_basket = product_basket.split(']')[0]
#         product_basket = product_basket.split(',')
#         a_list = []
#         for i in product_basket:
#             a_list.append(i.split('ProductBasket:')[1])
#         b_list = []
#         for i in a_list:
#             b_list.append(i.split('>')[0])
#         dict_c = {}
#         for i in b_list:
#             a = i.split(':')[0].strip()
#             b = i.split(':')[1].strip()
#             dict_c[a] = b
#         products = Product.objects.all()
#
#         for product in products:
#             for key, value in dict_c.items():
#                 if product.product == key:
#                     value = int(value)
#                     if product.balance < value:
#                         raise ValueError(f'В магазине нет столько товара. Вы хотите {value} а в наличии только {product.balance}')
#         username = self.request.POST.get('username')
#         address = self.request.POST.get('address')
#         phone = self.request.POST.get('phone')
#         if username == '' or address == '' or phone == '':
#             raise ValueError
#         order = Order(username=username, address=address, phone=phone)
#         order.save()
#         for product in products:
#
#             for key, value in dict_c.items():
#                 if product.product == key:
#                     order_product = OrderProduct()
#                     order_product.product = product
#                     order_product.order = order
#                     value = int(value)
#                     order_product.volume = value
#                     product.balance -= value
#                     order_product.save()
#                     product.save()
#         ProductBasket.objects.all().delete()
#         return redirect('product_basket_list_view')


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    # template_name = 'product_basket/product_basket_list_view.html'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     kwargs = super().get_context_data(object_list=object_list, kwargs=kwargs)
    #     products = ProductBasket.objects.all()
    #     kwargs['productbasket_list'] = products
    #     summ = []
    #     a = 0
    #     for product in products:
    #         total = product.product.price * product.volume
    #         a += total
    #         vol = product.volume
    #         p_id = product.id
    #         total = {'p_id': p_id, 'total': total, 'vol': vol}
    #         summ.append(total)
    #     kwargs['summ'] = summ
    #     kwargs['total'] = a
    #     kwargs['form'] = OrderForm()

        # return kwargs

    def form_valid(self, form):
        product_basket = self.request.POST.get('productbasket_list')
        if product_basket == '<QuerySet []>':
            return redirect('product_basket_list_view')
        product_basket = product_basket.split('[')[1]
        product_basket = product_basket.split(']')[0]
        product_basket = product_basket.split(',')
        a_list = []
        for i in product_basket:
            a_list.append(i.split('ProductBasket:')[1])
        b_list = []
        for i in a_list:
            b_list.append(i.split('>')[0])
        dict_c = {}
        for i in b_list:
            a = i.split(':')[0].strip()
            b = i.split(':')[1].strip()
            dict_c[a] = b
        products = Product.objects.all()

        for product in products:
            for key, value in dict_c.items():
                if product.product == key:
                    value = int(value)
                    if product.balance < value:
                        raise ValueError(
                            f'В магазине нет столько товара. Вы хотите {value} '
                            f'а в наличии только {product.balance}')
        order = form.save()
        for product in products:
            for key, value in dict_c.items():
                if product.product == key:
                    order_product = OrderProduct()
                    order_product.product = product
                    order_product.order = order
                    value = int(value)
                    order_product.volume = value
                    product.balance -= value
                    order_product.save()
                    product.save()
        ProductBasket.objects.all().delete()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('product_basket_list_view')
