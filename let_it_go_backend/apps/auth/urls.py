from django.urls import path

from let_it_go_backend.apps.auth.views import PasswordChangeView, SignInView
from let_it_go_backend.apps.user.views import UserViewSet

urlpatterns = [
    path("signup/", UserViewSet.as_view({"post": "create"}), name="signup"),
    path("signin/", SignInView.as_view(), name="signin"),
    path("password/change/", PasswordChangeView.as_view(), name="password-change"),
]
