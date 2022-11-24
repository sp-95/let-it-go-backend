from django.urls import path

from let_it_go_backend.apps.category import views

urlpatterns = [path("", views.CategoriesView.as_view(), name="categories")]
