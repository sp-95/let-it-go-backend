from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from let_it_go_backend.apps.category.models import Category
from let_it_go_backend.apps.product.models import Product
from let_it_go_backend.apps.product.permissions import ProductPermission
from let_it_go_backend.apps.product.serializers import (
    ProductSerializer,
    VerificationSerializer,
)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [ProductPermission]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["category", "condition", "owner", "verified"]
    search_fields = ["title", "description", "category"]

    def perform_create(self, serializer):
        category = Category.objects.get(id=self.request.data["category"])
        serializer.save(category=category, owner=self.request.user)


class VerificationView(UpdateAPIView):
    lookup_field = "id"
    serializer_class = VerificationSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        product_id = self.kwargs.get("id")
        product = Product.objects.filter(id=product_id)
        return product
