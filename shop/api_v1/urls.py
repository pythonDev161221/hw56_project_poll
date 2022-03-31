from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api_v1.views import ProductViewSet, OrderViewSet

product_router = routers.DefaultRouter()
product_router.register(r'products', ProductViewSet)
product_router.register(r'orders', OrderViewSet)


app_name = "api_v1"

urlpatterns = [
    path("", include(product_router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', obtain_auth_token, name='api_token_auth'),
]
