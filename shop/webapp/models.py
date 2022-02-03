from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.urls import reverse

CHOOSE_CATEGORY = [('other', 'разное'), ('clothes', 'одежда'), ('equipment', 'оборудование'), ('information', 'информативные')]


class Product(models.Model):
    product = models.CharField(max_length=100, null=False, blank=False, verbose_name="название")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="описание")
    category = models.CharField(max_length=100, null=False, blank=False, choices=CHOOSE_CATEGORY,
                                verbose_name="категории", default=CHOOSE_CATEGORY[0])
    balance = models.PositiveIntegerField(null=False, blank=False, verbose_name="остаток")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="цена", null=False, blank=False)

    def get_absolute_url(self):
        return reverse('product_list_view')

    def __str__(self):
        return f'{self.product}, {self.price}'
