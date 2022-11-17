from django.apps import AppConfig


class AuthConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "let_it_go_backend.apps.auth"
    label = "api_auth"
    verbose_name = "Authentication"
