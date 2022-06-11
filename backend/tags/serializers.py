from rest_framework import serializers

from tags.models import Tag


class TagSerializer(serializers.ModelSerializer):
    """Возвращает список тегов."""

    class Meta:
        model = Tag
        fields = '__all__'
