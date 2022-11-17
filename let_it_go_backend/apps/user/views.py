from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from let_it_go_backend.apps.user import serializers


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAdminUser]
