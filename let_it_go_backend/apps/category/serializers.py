from rest_framework import serializers

from let_it_go_backend.apps.category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)
