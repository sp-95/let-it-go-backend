from rest_framework import generics, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from let_it_go_backend.apps.auth.serializers import PasswordChangeSerializer


class SignInView(ObtainAuthToken):
    renderer_classes = (renderers.JSONRenderer, renderers.BrowsableAPIRenderer)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data["user"]
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "token": token.key,
                    "id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                }
            )
        except ValidationError as e:
            e.detail = " ".join(e.detail.get("non_field_errors", []))
            raise e


class PasswordChangeView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PasswordChangeSerializer

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj
