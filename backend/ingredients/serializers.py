from rest_framework import serializers

from ingredients.models import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    """
    Возвращает список всех ингридиентов,
    создает, изменяет и удаляет ингридиенты.
    """

    class Meta:
        model = Ingredient
        fields = '__all__'
        read_only_fields = ('id',)
