from rest_framework import serializers

from tags.models import Tag


class TagSerializer(serializers.ModelSerializer):
    """Возвращает список всех тегов, создает, изменяет и удаляет тег."""

    class Meta:
        model = Tag
        fields = '__all__'
        read_only_fields = ('id',)
