import django_filters as filters
from recipes.models import Recipe


class RecipeFilter(filters.FilterSet):
    """Фильтрация для рецепта по slug модели Tag."""
    tags = filters.AllValuesMultipleFilter(field_name='tags__slug')

    class Meta:
        model = Recipe
        fields = ('tags', 'author')
