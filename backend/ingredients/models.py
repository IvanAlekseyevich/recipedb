from django.db import models


class Ingredient(models.Model):
    name = models.CharField(
        verbose_name='название ингридиента',
        max_length=200
    )
    measurement_unit = models.CharField(
        verbose_name='единица измерения',
        max_length=200
    )
