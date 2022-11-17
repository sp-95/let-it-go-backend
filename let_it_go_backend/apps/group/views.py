from django.contrib.auth.models import Group
from rest_framework import permissions, viewsets

from let_it_go_backend.apps.group import serializers


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAdminUser]
