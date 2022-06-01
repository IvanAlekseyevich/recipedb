from django.contrib.auth import get_user_model
from rest_framework import serializers

from ingredients.serializers import IngredientAmountSerializer
from recipes.models import FavoriteRecipe, ShoppingCart, Recipe
from tags.serializers import TagSerializer
from users.models import Subscription

User = get_user_model()


class CustomSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'first_name', 'last_name', 'is_subscribed')

    def get_is_subscribed(self, obj):
        request_user = self.context.get('request').user.id
        queryset = Subscription.objects.filter(author=obj.id, subscriber=request_user).exists()
        return queryset


class RecipeSerializer(serializers.ModelSerializer):
    """"""
    tags = TagSerializer(many=True)
    author = CustomSerializer()
    ingredients = IngredientAmountSerializer(many=True)
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
        request_user = self.context.get('request').user.id
        queryset = FavoriteRecipe.objects.filter(user=request_user, recipe=obj).exists()
        return queryset

    def get_is_in_shopping_cart(self, obj):
        request_user = self.context.get('request').user.id
        queryset = ShoppingCart.objects.filter(user=request_user, recipe=obj).exists()
        return queryset


class TestRecipeSerializer(serializers.ModelSerializer):
    image = serializers.URLField

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'image', 'cooking_time')


class FavoriteRecipeSerializer(serializers.ModelSerializer):
    image = serializers.URLField

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'image', 'cooking_time')


class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = '__all__'
