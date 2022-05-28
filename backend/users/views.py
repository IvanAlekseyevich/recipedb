from rest_framework import viewsets

from users.models import User
from users.serializers import CustomUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Возвращает все теги, либо конкретный тег,
    создает/изменяет/удаляет теги.
    """
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = []


class Test1():
    pass


class Test2():
    pass


class Test3():
    pass


class Test4():
    pass
