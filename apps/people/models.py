from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Range(models.Model):
    range_name = models.CharField(max_length=100)
    multiplier = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(9)]
    )

    def __str__(self):
        return f"{self.range_name} (Multiplier: {self.multiplier})"
