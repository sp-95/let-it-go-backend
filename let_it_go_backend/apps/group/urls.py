from django.urls import include, path
from rest_framework.routers import DefaultRouter

from let_it_go_backend.apps.group import views

router = DefaultRouter()
router.register("", views.GroupViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
