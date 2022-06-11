from rest_framework import filters, viewsets

from ingredients.models import Ingredient
from ingredients.permissions import ReadOnly
from ingredients.serializers import IngredientSerializer


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    """Возвращает список ингредиентов с возможностью поиска по имени."""
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [ReadOnly]
    filter_backends = (filters.SearchFilter,)
    pagination_class = None
    search_fields = ('^name',)
