from rest_framework import viewsets

from tags.models import Tag
from tags.serializers import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    Возвращает список тегов, либо конкретный тег,
    создает/изменяет/удаляет тег.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None
    permission_classes = []
