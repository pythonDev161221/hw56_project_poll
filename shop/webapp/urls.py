from django.urls import path

from webapp.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    AddProductBasketView, ProductBasketDeleteView, OrderCreateView, ProductBasketListView, ProductBasketOneDeleteView, \
    AddMultipleProductBasketView

app_name = 'webapp'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list_view'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail_view'),
    path('product/create/', ProductCreateView.as_view(), name='product_create_view'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update_view'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete_view'),
    path('product/<int:pk>/basket/add/', AddProductBasketView.as_view(), name='product_basket_add_view'),
    path('basket/', ProductBasketListView.as_view(), name='product_basket_list_view'),
    path('basket/<int:pk>/delete/', ProductBasketDeleteView.as_view(), name='product_basket_delete_view'),
    path('order/create/', OrderCreateView.as_view(), name='order_create_view'),
    path('basket/<int:pk>/delete_one/', ProductBasketOneDeleteView.as_view(), name='product_basket_one_delete_view'),
    path('product/<int:pk>/basket/add/multiple/', AddMultipleProductBasketView.as_view(),
         name='add_multiple_product_basket_view'),

]
