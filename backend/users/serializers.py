from django.contrib.auth import get_user_model
from djoser import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from recipes.models import Recipe
from recipes.serializers import ShortRecipeSerializer
from users.models import Subscription

User = get_user_model()


class CustomUserSerializer(serializers.UserSerializer):
    """
    Cериализатор пользователя для djoser. Возвращает список
    пользователей, либо одного пользователя и изменяет его.
    """
    is_subscribed = SerializerMethodField()

    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'first_name', 'last_name', 'is_subscribed')

    def get_is_subscribed(self, obj):
        """
        Добавляет поле подписки - подписан ли текущий пользователь
        на этого пользователя: true/false.
        """
        request_user = self.context.get('request').user.id
        queryset = Subscription.objects.filter(author=obj.id, subscriber=request_user).exists()
        return queryset

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError('Нельзя использовать имя <me>!')
        return value


class CustomUserCreateSerializer(serializers.UserCreateSerializer):
    """Cериализатор создания пользователя для djoser."""

    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'password', 'first_name', 'last_name')

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError('Нельзя использовать имя <me>!')
        return value


class CustomUserDeleteSerializer(ModelSerializer):
    """Cериализатор удаления пользователя для djoser."""

    class Meta:
        model = User
        fields = ''


class SubscriptionsSerializer(ModelSerializer):
    """
    Возвращает список подписок данного пользователя на других пользователей,
    либо один профиль пользователя при подписке на него.
    """
    recipes = ShortRecipeSerializer(read_only=True, many=True)
    recipes_count = SerializerMethodField()

    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'first_name', 'last_name',
                  'recipes', 'recipes_count')

    def get_recipes_count(self, obj):
        """Добавляет поле с количеством рецептов данного пользователя."""
        queryset = Recipe.objects.filter(author=obj).count()
        return queryset
