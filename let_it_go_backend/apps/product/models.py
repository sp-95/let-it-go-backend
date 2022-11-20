from django.db import models

from let_it_go_backend.apps.core.models import AbstractBaseModel


class Product(AbstractBaseModel):
    title = models.CharField(max_length=60)
    price = models.FloatField()
    category = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    image = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} ({self.category}): ${self.price}"
