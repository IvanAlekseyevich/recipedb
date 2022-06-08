from rest_framework import filters, viewsets

from ingredients.models import Ingredient
from ingredients.permissions import IsAdminOrReadOnly
from ingredients.serializers import IngredientSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    """
    Возвращает список ингридиентов, либо конкретный ингридиент,
    создает/изменяет/удаляет ингридиент.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = (filters.SearchFilter,)
    pagination_class = None
    search_fields = ('^name',)
