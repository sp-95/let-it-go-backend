from rest_framework import viewsets

from let_it_go_backend.apps.product.models import Product
from let_it_go_backend.apps.product.permissions import ProductPermission
from let_it_go_backend.apps.product.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [ProductPermission]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
