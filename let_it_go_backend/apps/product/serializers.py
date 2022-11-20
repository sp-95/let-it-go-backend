from rest_framework import serializers

from let_it_go_backend.apps.product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ["user"]
