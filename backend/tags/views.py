from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tags.models import Tag
from tags.serializers import TagSerializer


class AllTagsView(APIView):
    """Возвращает все теги, создает теги."""

    # permission_classes = []
    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagView(APIView):
    """Возвращает конкретный тег, изменяет и удаляет его."""

    # permission_classes = []
    def get(self, request, tag_id):
        current_tag = get_object_or_404(Tag, id=tag_id)
        serializer = TagSerializer(current_tag)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, tag_id):
        current_tag = get_object_or_404(Tag, id=tag_id)
        serializer = TagSerializer(
            current_tag,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, tag_id):
        current_tag = get_object_or_404(Tag, id=tag_id)
        current_tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
