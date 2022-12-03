from django.urls import path
from rest_framework.routers import DefaultRouter

from let_it_go_backend.apps.product import views

router = DefaultRouter()
router.register("", views.ProductViewSet)


urlpatterns = [
    path("verify/<int:id>/", views.VerificationView.as_view(), name="verify_product"),
]

urlpatterns += router.urls
