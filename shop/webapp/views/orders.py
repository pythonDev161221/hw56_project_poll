from django.shortcuts import redirect
from django.views import View


class OrderCreateView(View):
    def post(self, request, *args, **kwargs):
        product_basket = self.request.POST.get('productbasket_list')
        product_basket = product_basket.split('[')[1]
        product_basket = product_basket.split(']')[0]
        product_basket = product_basket.split(',')
        a_list = []
        for i in product_basket:
            a_list.append(i.split('ProductBasket:')[1])
        b_list = []
        for i in a_list:
            b_list.append(i.split('>')[0])
        print(b_list)
        dict_c = {}
        for i in b_list:
            a = i.split(':')[0].strip()
            b = i.split(':')[1].strip()
            dict_c[a] = b
        print(dict_c)


        context = {}
        # for i, j in request.GET:
        #     print(i)
        #     print(j)
        #     context['i'] = j
        # print(context)

        return redirect('product_list_view')
