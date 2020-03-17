from django.core.validators import MinLengthValidator
from django.db import models
from model_utils.models import TimeStampedModel


class Item(TimeStampedModel):
    class Kinds(models.TextChoices):
        BOOKMARK = "bookmark"

    key = models.CharField(
        "Label of the item", max_length=20, validators=[MinLengthValidator(1)]
    )
    value = models.TextField("Value of the item", validators=[MinLengthValidator(1)])
    kind = models.CharField(
        "Type of item", max_length=20, choices=Kinds.choices, default=Kinds.BOOKMARK
    )
