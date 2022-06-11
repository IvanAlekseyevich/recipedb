from django.db import models


class Tag(models.Model):
    """
    Создает объект тэг со следующими обязательными уникальными атрибутами:
    - name
    - color
    - slug
    """
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        unique=True
    )
    color = models.CharField(
        verbose_name='Цвет в HEX',
        max_length=7,
        unique=True
    )
    slug = models.SlugField(
        verbose_name='Уникальный слаг',
        max_length=200,
        unique=True
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name
