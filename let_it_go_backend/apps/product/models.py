from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from let_it_go_backend.apps.core.models import AbstractBaseModel


class Product(AbstractBaseModel):
    class Condition(models.IntegerChoices):
        POOR = 1, _("Poor")
        OKAY = 2, _("Okay")
        GOOD = 3, _("Good")
        GREAT = 4, _("Great")
        NEW = 5, _("New")

    title = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=60)
    price = models.DecimalField(
        decimal_places=2, max_digits=12, validators=[MinValueValidator(0)]
    )
    image = models.CharField(max_length=255)
    condition = models.IntegerField(choices=Condition.choices, default=Condition.GOOD)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title} ({self.category}): ${self.price}"
