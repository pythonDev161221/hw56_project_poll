from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api_v1.serializers import ProductSerializer, OrderSerializer
from webapp.models import Product, Order


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)


@ensure_csrf_cookie
def get_csrf_token_view(request):
    if request.method == "GET":
        return HttpResponse()
    return HttpResponseNotAllowed(["GET"])

