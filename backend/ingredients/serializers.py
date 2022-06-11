from rest_framework import serializers

from ingredients.models import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    """Возвращает список ингридиентов."""

    class Meta:
        model = Ingredient
        fields = '__all__'
