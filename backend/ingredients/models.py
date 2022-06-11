from django.db import models


class Ingredient(models.Model):
    """
    Создает объект ингридиента со следующими обязательными атрибутами:
    - name
    - measurement_unit
    """
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
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'measurement_unit'],
                name='ingredient'
            )
        ]

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'
