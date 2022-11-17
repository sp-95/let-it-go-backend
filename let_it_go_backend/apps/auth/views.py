from rest_framework import renderers
from rest_framework.authtoken.views import ObtainAuthToken


class LoginView(ObtainAuthToken):
    renderer_classes = (renderers.JSONRenderer, renderers.BrowsableAPIRenderer)
