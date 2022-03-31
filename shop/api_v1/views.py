from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from api_v1.serializers import ProductSerializer, OrderSerializer
from webapp.models import Product, Order


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(ModelViewSet):
   queryset = Order.objects.all()
   serializer_class = OrderSerializer