from rest_framework import mixins, viewsets

from ingredients.models import Ingredient
from ingredients.serializers import IngredientsSerializer


class IngredientsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientsSerializer
    # permission_classes = [IsAdmin]
