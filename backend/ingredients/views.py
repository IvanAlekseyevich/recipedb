from rest_framework import viewsets

from ingredients.models import Ingredient
from ingredients.serializers import IngredientSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    """
    Возвращает все ингридиенты, либо конкретный ингридиент,
    создает/изменяет/удаляет ингридиенты.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    pagination_class = None
    permission_classes = []
