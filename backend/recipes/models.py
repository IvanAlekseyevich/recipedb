from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

User = get_user_model()


class Ingredient(models.Model):
    """
    Создает объект ингридиент со следующими обязательными атрибутами:
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


class Recipe(models.Model):
    """
    Создает объект рецепт со следующими обязательными атрибутами:
    - author
    - name
    - image
    - text
    - ingredients
    - tags
    - cooking_time
    - pub_date
    """
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор'
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=200
    )
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='recipes/images/'
    )
    text = models.TextField(
        verbose_name='Описание'
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='recipes',
        through='RecipeIngredient',
        verbose_name='Ингридиенты'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        through='RecipeTag',
        verbose_name='Тэг'
    )
    cooking_time = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1, 'Время приготовления не может быть меньше минуты!')],
        verbose_name='Время приготовления (в минутах)'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации рецепта',
        auto_now_add=True
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    """
    Промежуточная модель, связывающая модель рецепт и ингридиент,
    имеет следующие атрибуты:
    - recipe
    - ingredient
    - amount
    """
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingridientamount',
        verbose_name='Рецепт'
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='ingridientamount',
        verbose_name='Ингридиент'
    )
    amount = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1, 'Убедитесь, что это значение больше либо равно 1.')],
        verbose_name='Количество ингридиента'
    )

    class Meta:
        ordering = ['recipe']
        verbose_name = 'Ингридиенты'
        verbose_name_plural = 'Ингридиенты и их количество'
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='recipeingredient'
            )
        ]

    def __str__(self):
        return f'{self.recipe} - {self.ingredient} {self.amount}'


class RecipeTag(models.Model):
    """
    Промежуточная модель, связывающая модель рецепт и тег,
    имеет следующие атрибуты:
    - recipe
    - tag
    """
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт'
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        verbose_name='Тэг'
    )

    class Meta:
        ordering = ['recipe']
        verbose_name = 'Тэги'
        verbose_name_plural = 'Теги рецептов'
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'tag'],
                name='recipetag'
            )
        ]

    def __str__(self):
        return f'{self.recipe} - {self.tag}'


class FavoriteRecipe(models.Model):
    """
    Создает объект избраного рецепта со следующими атрибутами:
    - user
    - recipe
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorite',
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorite',
        verbose_name='Рецепт'
    )

    class Meta:
        ordering = ['user']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Избранные рецепты'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='favoriterecipe'
            )
        ]

    def __str__(self):
        return self.user


class ShoppingCart(models.Model):
    """
    Создает объект списка покупок со следующими атрибутами:
    - user
    - recipe
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping',
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shopping',
        verbose_name='Рецепт'
    )

    class Meta:
        ordering = ['user']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Списки покупок'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='shoppingcart'
            )
        ]

    def __str__(self):
        return f'{self.user} - {self.recipe}'
