from django.urls import path
from rest_framework.routers import DefaultRouter

from let_it_go_backend.apps.product import views

router = DefaultRouter()
router.register("", views.ProductViewSet)


urlpatterns = [
    path("<uuid:id>/contact/", views.ContactView.as_view(), name="contact_seller"),
    path("<uuid:id>/verify/", views.VerificationView.as_view(), name="verify_product"),
]

urlpatterns += router.urls
