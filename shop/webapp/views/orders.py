from django.shortcuts import redirect
from django.views import View

from webapp.models import Product, ProductBasket


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
                        raise ValueError(f'В магазине нет столько. Вы хотите {value} а в наличии только {product.balance}')
                    product.balance -= value
                    product.save()
        ProductBasket.objects.all().delete()
        return redirect('product_basket_list_view')
