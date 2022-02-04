from django.contrib import admin

# Register your models here.
from webapp.models import Product, ProductBasket

admin.site.register(Product)
admin.site.register(ProductBasket)