from rest_framework import serializers

from let_it_go_backend.apps.product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    owner_first_name = serializers.CharField(source="owner.first_name", read_only=True)
    owner_last_name = serializers.CharField(source="owner.last_name", read_only=True)
    owner_email = serializers.CharField(source="owner.email", read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ("owner",)
