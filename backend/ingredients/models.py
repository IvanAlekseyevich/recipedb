from django.core.validators import MinValueValidator
from django.db import models


class Ingredient(models.Model):
    """Содержит ингридиенты."""
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        db_index=True
    )
    measurement_unit = models.CharField(
        verbose_name='Единицы измерения',
        max_length=200
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'

    def __str__(self):
        return self.name


class IngredientAmount(models.Model):
    """Содержит ингридиенты и их количество из рецептов."""
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Ингридиент',
        max_length=200,
        db_index=True
    )
    amount = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1, 'Убедитесь, что это значение больше либо равно 1.')],
        verbose_name='Количество'
    )

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Ингридиенты и их количество'

