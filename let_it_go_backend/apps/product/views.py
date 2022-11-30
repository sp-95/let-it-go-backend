from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from let_it_go_backend.apps.category.models import Category
from let_it_go_backend.apps.product.models import Product
from let_it_go_backend.apps.product.permissions import ProductPermission
from let_it_go_backend.apps.product.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [ProductPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["category", "condition", "owner"]
    search_fields = ["title", "description", "category"]

    def perform_create(self, serializer):
        category = Category.objects.get(pk=self.request.data["category"])
        serializer.save(category=category, owner=self.request.user)
