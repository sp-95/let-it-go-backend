from django.urls import path

from let_it_go_backend.apps.auth.views import LoginView
from let_it_go_backend.apps.user.views import UserViewSet

urlpatterns = [
    path("signup/", UserViewSet.as_view({"post": "create"}), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
]
