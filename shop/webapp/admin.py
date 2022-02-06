from django.contrib import admin

# Register your models here.
from webapp.models import Product, ProductBasket, Order, OrderProduct

admin.site.register(Product)
admin.site.register(ProductBasket)
admin.site.register(Order)
admin.site.register(OrderProduct)
