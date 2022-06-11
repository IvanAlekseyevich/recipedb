from rest_framework import serializers

from ingredients.models import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    """Возвращает список ингридиентов, либо выбранный ингридиент."""

    class Meta:
        model = Ingredient
        fields = '__all__'
