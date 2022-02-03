from django.urls import path

from webapp.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list_view'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail_view'),
    path('product/create/', ProductCreateView.as_view(), name='product_create_view'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update_view'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete_view'),
]
