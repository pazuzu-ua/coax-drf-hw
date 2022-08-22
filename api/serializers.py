from rest_framework.serializers import ModelSerializer
from .models import Product, Order


class ProductSerializer(ModelSerializer):
    """This is a product serializer."""

    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(ModelSerializer):
    """This is an order serializer."""

    class Meta:
        model = Order
        fields = '__all__'
