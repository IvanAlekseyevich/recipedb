from django.db import models


class Tag(models.Model):
    name = models.CharField(
        verbose_name='название тэга',
        max_length=200,
        unique=True
    )
    color = models.CharField(
        verbose_name='цвет тэга в HEX',
        max_length=7,
        unique=True
    )
    slug = models.SlugField(
        verbose_name='сокращение тэга',
        max_length=200,
        unique=True
    )
