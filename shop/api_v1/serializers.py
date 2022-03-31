from rest_framework import serializers

from webapp.models import Product, OrderProduct, Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "product", "description", "category", "balance", "price")
        read_only_fields = ("id",)


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ('id', 'order', 'product', 'volume')


class OrderSerializer(serializers.ModelSerializer):
    order_products = OrderProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('user', 'phone', 'created_at', 'order_products')
