from django.contrib.auth import get_user_model
from djoser import serializers
from rest_framework.serializers import ModelSerializer

User = get_user_model()


class CustomUserSerializer(serializers.UserSerializer):
    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'first_name', 'last_name')

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
