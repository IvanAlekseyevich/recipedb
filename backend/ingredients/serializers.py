from rest_framework import serializers

from ingredients.models import Ingredient, IngredientAmount


class IngredientSerializer(serializers.ModelSerializer):
    """
    Возвращает список всех ингридиентов,
    создает, изменяет и удаляет ингридиенты.
    """

    class Meta:
        model = Ingredient
        fields = '__all__'
        read_only_fields = ('id',)


class IngredientAmountSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    measurement_unit = serializers.SerializerMethodField()

    class Meta:
        model = IngredientAmount
        fields = ('id', 'name', 'measurement_unit', 'amount')
        read_only_fields = ('id',)

    def get_name(self, obj):
        return obj.ingredient.name

    def get_measurement_unit(self, obj):
        return obj.ingredient.measurement_unit
