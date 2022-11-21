from rest_framework import generics, renderers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from let_it_go_backend.apps.auth.serializers import PasswordChangeSerializer


class SignInView(ObtainAuthToken):
    renderer_classes = (renderers.JSONRenderer, renderers.BrowsableAPIRenderer)

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request=request, *args, **kwargs)
        except ValidationError as e:
            e.detail = " ".join(e.detail.get("non_field_errors", []))
            raise e


class PasswordChangeView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PasswordChangeSerializer

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj
