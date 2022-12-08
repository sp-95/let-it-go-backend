from rest_framework import serializers

from let_it_go_backend.apps.product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name", read_only=True)
    owner_id = serializers.IntegerField(source="owner.id", read_only=True)
    owner_first_name = serializers.CharField(source="owner.first_name", read_only=True)
    owner_last_name = serializers.CharField(source="owner.last_name", read_only=True)
    owner_email = serializers.CharField(source="owner.email", read_only=True)

    class Meta:
        model = Product
        exclude = ["owner"]
        read_only_fields = ["verified"]

    def run_validation(self, data=...):
        image = data.get("image")
        if image and isinstance(image, str):
            request = self.context.get("request")
            current_image = Product.objects.get(pk=self.initial_data["id"])
            current_image_url = request.build_absolute_uri(current_image.image.url)
            if current_image_url == image:
                data.pop("image", None)
        return super().run_validation(data)


class ContactSerializer(serializers.Serializer):
    pass


class VerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "verified"]
