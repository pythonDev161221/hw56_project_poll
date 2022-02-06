from django.shortcuts import redirect
from django.views import View

from webapp.forms import OrderForm
from webapp.models import Product, ProductBasket, Order, OrderProduct


class OrderCreateView(View):
    def post(self, request, *args, **kwargs):
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
                        raise ValueError(f'В магазине нет столько товара. Вы хотите {value} а в наличии только {product.balance}')
        username = self.request.POST.get('username')
        print(username)
        address = self.request.POST.get('address')
        phone = self.request.POST.get('phone')
        order = Order(username=username, address=address, phone=phone)
        # order = Order()
        # order.username = username
        print(order.username)
        order.save()
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
        return redirect('product_basket_list_view')
