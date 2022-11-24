from rest_framework.routers import DefaultRouter

from let_it_go_backend.apps.product import views

router = DefaultRouter()
router.register("", views.ProductViewSet)


urlpatterns = [
    # Other APIs here
]

urlpatterns += router.urls
