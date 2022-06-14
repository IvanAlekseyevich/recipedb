from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from recipes.models import Recipe
from users.models import Subscription

User = get_user_model()


class IsSubscribedMixin(serializers.Serializer):
    """
    Добавляет поле подписки в сериализатор - подписан ли
    текущий пользователь на этого пользователя: true/false.
    Необходим доступ к request из context.
    """
    is_subscribed = serializers.SerializerMethodField()

    def get_is_subscribed(self, obj):
        request_user = self.context.get('request').user.id
        return Subscription.objects.filter(author=obj.id, subscriber=request_user).exists()


class CustomUserSerializer(UserSerializer, IsSubscribedMixin):
    """
    Cериализатор пользователя для djoser. Возвращает список
    пользователей либо одного пользователя и изменяет его.
    """

    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'first_name', 'last_name', 'is_subscribed')


class CustomUserCreateSerializer(UserCreateSerializer):
    """Cериализатор создания пользователя для djoser."""

    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'password', 'first_name', 'last_name')


class CustomUserDeleteSerializer(serializers.ModelSerializer):
    """Cериализатор удаления пользователя для djoser."""

    class Meta:
        model = User
        fields = ''


class RecipeMinifiedSerializer(serializers.ModelSerializer):
    """Выводит укороченный список атрибутов рецепта."""
    image = serializers.URLField

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'image', 'cooking_time')


class UserWithRecipesSerializer(serializers.ModelSerializer, IsSubscribedMixin):
    """
    Возвращает список подписок данного пользователя на других пользователей,
    либо профиль пользователя на которого подписываешься.
    """
    recipes = RecipeMinifiedSerializer(read_only=True, many=True)
    recipes_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'first_name', 'last_name',
                  'is_subscribed', 'recipes', 'recipes_count')

    def get_recipes_count(self, obj):
        """Добавляет поле с общим количеством рецептов пользователя."""
        return obj.recipes.count()
