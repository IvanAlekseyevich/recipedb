from rest_framework import viewsets

from tags.models import Tag
from tags.permissions import IsAdminOrReadOnly
from tags.serializers import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    Возвращает список тегов, либо конкретный тег,
    создает/изменяет/удаляет тег.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = None
