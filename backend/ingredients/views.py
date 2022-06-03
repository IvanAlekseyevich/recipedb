from rest_framework import filters
from rest_framework import viewsets

from ingredients.models import Ingredient
from ingredients.serializers import IngredientSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    """
    Возвращает список ингридиентов, либо конкретный ингридиент,
    создает/изменяет/удаляет ингридиент.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = []
    filter_backends = (filters.SearchFilter,)
    pagination_class = None
    search_fields = ('^name',)
