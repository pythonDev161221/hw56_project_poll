from django.contrib.auth import get_user_model
from django.contrib.sessions.models import Session
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.urls import reverse

from webapp.validators import MinValueValidator

User = get_user_model()

CHOOSE_CATEGORY = [('other', 'разное'), ('clothes', 'одежда'), ('equipment', 'оборудование'), ('information', 'информативные')]


class Product(models.Model):
    product = models.CharField(max_length=100, null=False, blank=False, verbose_name="название")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="описание")
    category = models.CharField(max_length=100, null=False, blank=False, choices=CHOOSE_CATEGORY,
                                verbose_name="категории", default=CHOOSE_CATEGORY[0])
    balance = models.PositiveIntegerField(null=False, blank=False, verbose_name="остаток", validators=(MinValueValidator(0),))
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="цена", null=False, blank=False, validators=(MinValueValidator(0),))

    def get_absolute_url(self):
        return reverse('webapp:product_list_view')

    def __str__(self):
        return f'{self.product}, {self.price}'


class ProductBasket(models.Model):
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, related_name='products_basket',
                                verbose_name='Корзина')
    volume = models.PositiveIntegerField()
    session = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return f'{self.product.product}: {self.volume}'


class OrderProduct(models.Model):
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE)
    order = models.ForeignKey('webapp.Order', on_delete=models.CASCADE)
    volume = models.PositiveIntegerField()


class Order(models.Model):
    products = models.ManyToManyField('webapp.Product',
                related_name='orders', through='webapp.OrderProduct')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1,
                             related_name="orders")
    phone = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
