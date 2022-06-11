from rest_framework import viewsets

from tags.models import Tag
from tags.permissions import ReadOnly
from tags.serializers import TagSerializer


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    """Возвращает список тегов."""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [ReadOnly]
    pagination_class = None
