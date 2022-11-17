from django.urls import path

from let_it_go_backend.apps.user import views

urlpatterns = [
    path("signup/", views.UserViewSet.as_view({"post": "create"}), name="signup"),
]
