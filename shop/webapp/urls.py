from django.urls import path

from webapp.views import ProductListView, ProductDetailView, ProductCreateView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list_view'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail_view'),
    path('product/create/', ProductCreateView.as_view(), name='product_create_view'),
]
