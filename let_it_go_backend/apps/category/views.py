from rest_framework import generics, permissions

from let_it_go_backend.apps.category.models import Category
from let_it_go_backend.apps.category.serializers import CategorySerializer


class CategoriesView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
