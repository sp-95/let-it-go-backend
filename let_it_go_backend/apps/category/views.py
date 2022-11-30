from rest_framework.generics import ListAPIView

from let_it_go_backend.apps.category.models import Category
from let_it_go_backend.apps.category.serializers import CategorySerializer
from let_it_go_backend.apps.core.permissions import IsAdminOrReadOnly


class CategoriesView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
