from rest_framework import mixins, viewsets

from tags.models import Tag
from tags.serializers import TagSerializer


class TagViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # permission_classes = [IsAdmin]
