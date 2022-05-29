from django.contrib.auth import get_user_model
from djoser import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from recipes.models import Recipe
from users.models import Subscription

User = get_user_model()


class CustomUserSerializer(serializers.UserSerializer):
    is_subscribed = SerializerMethodField()

    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'first_name', 'last_name', 'is_subscribed')

    def get_is_subscribed(self, obj):
        request_user = self.context.get('request').user.id
        queryset = Subscription.objects.filter(author=obj.id, subscriber=request_user).exists()
        return queryset

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError('Нельзя использовать имя <me>!')
        return value


class CustomUserCreateSerializer(serializers.UserCreateSerializer):
    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'password', 'first_name', 'last_name')

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError('Нельзя использовать имя <me>!')
        return value


class CustomUserDeleteSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ''


class SubscriptionsSerializer(ModelSerializer):
    # recipes = RecipesSerializer(read_only=True, many=True)
    # recipes_count = SerializerMethodField()
    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'password', 'first_name', 'last_name')
        # fields = ('email', 'id', 'username', 'password', 'first_name', 'last_name',
        #           'recipes', 'recipes_count')

    # def get_is_subscribed(self, obj):
    #     queryset = Recipe.objects.filter(author=obj.id).count()
    #     return queryset

