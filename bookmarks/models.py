from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from model_utils.models import TimeStampedModel


class Item(TimeStampedModel):
    class Kinds(models.TextChoices):
        BOOKMARK = "bookmark"

    key = models.CharField(max_length=20, validators=[MinLengthValidator(1)])
    value = models.TextField(validators=[MinLengthValidator(1)])
    kind = models.CharField(
        max_length=20, choices=Kinds.choices, default=Kinds.BOOKMARK
    )
    row = models.IntegerField(MinValueValidator(0),)
    collection = models.ForeignKey("Collection", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.key}::{self.row}::{self.collection.key}"


class Collection(TimeStampedModel):
    key = models.CharField(max_length=20, validators=[MinLengthValidator(1)])
    column = models.IntegerField(MinValueValidator(0))
    row = models.IntegerField(MinValueValidator(0),)

    def __str__(self):
        return f"{self.key}::{self.column}::{self.row}"
