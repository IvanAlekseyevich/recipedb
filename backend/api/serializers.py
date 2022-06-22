from django.contrib.auth import get_user_model
from drf_extra_fields.fields import Base64ImageField
from recipes.models import (FavoriteRecipe, Ingredient, Recipe,
                            RecipeIngredient, RecipeTag, ShoppingCart, Tag)
from rest_framework import serializers
from users.serializers import CustomUserSerializer

User = get_user_model()


class IngredientSerializer(serializers.ModelSerializer):
    """Возвращает список ингридиентов."""

    class Meta:
        model = Ingredient
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    """Возвращает список тегов."""

    class Meta:
        model = Tag
        fields = '__all__'


class IngredientInRecipeSerializer(serializers.ModelSerializer):
    """Возвращает ингридиент, его единицу измерения и количество из рецепта."""
    id = serializers.ReadOnlyField(source='ingredient.id')
    name = serializers.ReadOnlyField(source='ingredient.name')
    measurement_unit = serializers.ReadOnlyField(source='ingredient.measurement_unit')

    class Meta:
        model = RecipeIngredient
        fields = ('id', 'name', 'measurement_unit', 'amount')


class RecipeListSerializer(serializers.ModelSerializer):
    """Возвращает рецепт, либо список рецептов."""
    tags = TagSerializer(many=True)
    author = CustomUserSerializer()
    ingredients = IngredientInRecipeSerializer(source="ingridientamount", many=True)
    is_favorited = serializers.SerializerMethodField()
    is_in_shopping_cart = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = (
            'id',
            'tags',
            'author',
            'ingredients',
            'is_favorited',
            'is_in_shopping_cart',
            'name',
            'image',
            'text',
            'cooking_time'
        )
        read_only_fields = ('id',)

    def get_is_favorited(self, obj):
        """
        Добавляет поле избранного - есть ли данный рецепт у
        текущего пользователя в избранном: true/false.
        """
        request_user = self.context.get('request').user.id
        return FavoriteRecipe.objects.filter(user=request_user, recipe=obj).exists()

    def get_is_in_shopping_cart(self, obj):
        """
        Добавляет поле списка покупок - есть ли данный рецепт у
        текущего пользователя в списке покупок: true/false.
        """
        request_user = self.context.get('request').user.id
        return ShoppingCart.objects.filter(user=request_user, recipe=obj).exists()


class IngridCreateSerializer(serializers.ModelSerializer):
    """Создает запись в таблице RecipeIngredient."""
    id = serializers.PrimaryKeyRelatedField(queryset=Ingredient.objects.all())
    amount = serializers.IntegerField(write_only=True, min_value=1)

    class Meta:
        model = RecipeIngredient
        fields = ('id', 'amount')


class RecipeCreateUpdateSerializer(serializers.ModelSerializer):
    """Создает, либо изменяет рецепт."""
    ingredients = IngridCreateSerializer(many=True)
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)
    image = Base64ImageField()
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate(self, data):
        ingredients = data.get('ingredients')
        tags = data.get('tags')
        if len(ingredients) == 0 or len(tags) == 0:
            raise serializers.ValidationError('Заполните все необходимые поля')
        return data

    class Meta:
        model = Recipe
        fields = (
            'author',
            'ingredients',
            'tags',
            'image',
            'name',
            'text',
            'cooking_time'
        )

    def to_representation(self, instance):
        """Изменяет вывод созданного рецепта."""
        return RecipeListSerializer(instance, context=self.context).data

    def create(self, validated_data):
        """Создает рецепт."""
        ingredients = validated_data.pop('ingredients')
        tags = validated_data.pop('tags')
        recipe = Recipe.objects.create(**validated_data)
        for ingredient in ingredients:
            RecipeIngredient.objects.create(recipe=recipe, ingredient=ingredient['id'],
                                            amount=ingredient['amount'])
        for tag in tags:
            RecipeTag.objects.create(recipe=recipe, tag=tag)
        return recipe

    def update(self, instance, validated_data):
        """Изменяет рецепт."""
        instance.name = validated_data.get('name', instance.name)
        instance.text = validated_data.get('text', instance.text)
        instance.cooking_time = validated_data.get('cooking_time', instance.cooking_time)
        instance.image = validated_data.get('image', instance.image)
        ingredients = validated_data.pop('ingredients')
        tags = validated_data.pop('tags')
        recipe_ingr = RecipeIngredient.objects.filter(recipe=instance)
        recipe_ingr.delete()
        for ingredient in ingredients:
            RecipeIngredient.objects.create(recipe=instance, ingredient=ingredient['id'],
                                            amount=ingredient['amount'])
        tags_recipe = RecipeTag.objects.filter(recipe=instance)
        tags_recipe.delete()
        for tag in tags:
            RecipeTag.objects.create(recipe=instance, tag=tag)
        instance.save()
        return instance


class ShoppingCartSerializer(serializers.ModelSerializer):
    """Выводит список рецептов, добавленных в список покупок."""

    class Meta:
        model = ShoppingCart
        fields = '__all__'
