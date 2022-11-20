"""let_it_go_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
]

api_urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("auth/", include("let_it_go_backend.apps.auth.urls")),
    path("users/", include("let_it_go_backend.apps.user.urls")),
    path("groups/", include("let_it_go_backend.apps.group.urls")),
    path("products/", include("let_it_go_backend.apps.product.urls")),
]

# API v1 URL endpoints
urlpatterns += [
    path("api/v1/", include(api_urlpatterns)),
]
