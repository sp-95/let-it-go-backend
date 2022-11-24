from django.db import models

from let_it_go_backend.apps.core.models import AbstractBaseModel


class Category(AbstractBaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
