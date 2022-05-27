from rest_framework import viewsets

from tags.models import Tag
from tags.serializers import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    Возвращает все теги, либо конкретный тег,
    создает/изменяет/удаляет теги.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None
    permission_classes = []
