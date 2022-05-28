from rest_framework import viewsets

from users import serializers
from users.models import User


class UserViewSet(viewsets.ModelViewSet):
    """
    Возвращает всех пользователей, либо конкретного
    пользователя, создает/изменяет/удаляет пользователей.
    """
    queryset = User.objects.all()
    permission_classes = []

    # def get_queryset(self):
    #     is_subscribed = Subscription.objects.filter(subscriber=self.request.user).exist()
    #     queryset = User.objects.annotate(is_subscribed=is_subscribed)
    #     return queryset
    def me(self):
        user = self.request.user
        queryset = User.objects.get(pk=user.pk)
        return queryset

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.CustomUserCreateSerializer

        return serializers.CustomUserSerializer


class Test1():
    pass


class Test2():
    pass


class Test3():
    pass


class Test4():
    pass
