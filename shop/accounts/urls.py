from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import RegisterView, UserBasketDetailView, UserOrderDetailView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('registration/', RegisterView.as_view(), name='registration'),
    path('user/<int:pk>/basket/', UserBasketDetailView.as_view(), name='user_basket_detail_view'),
    path('order/<int:pk>/', UserOrderDetailView.as_view(), name='user_order_detail_view'),
]
