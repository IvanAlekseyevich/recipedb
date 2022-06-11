from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from users import serializers
from users.models import Subscription, User


class SubscriptionsApiView(APIView):
    """Возвращает список подписок текущего пользователя на других пользователей."""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        authors = User.objects.filter(subscribers__subscriber=user)
        serializer = serializers.SubscriptionsSerializer(
            authors,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubscribeApiView(APIView):
    """Добавляет либо удаляет подписку на данного пользователя."""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        author = get_object_or_404(User, id=user_id)
        user = request.user
        if author == user:
            return Response(
                {"errors": "Нельзя подписываться на самого себя!"},
                status=status.HTTP_400_BAD_REQUEST
            )
        if Subscription.objects.filter(author=author, subscriber=user).exists():
            return Response(
                {"errors": "Вы уже подписаны на данного пользователя."},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            Subscription.objects.create(author=author, subscriber=user)
            serializer = serializers.SubscriptionsSerializer(author, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, user_id):
        author = get_object_or_404(User, id=user_id)
        user = request.user
        if Subscription.objects.filter(author=author, subscriber=user).exists():
            Subscription.objects.get(author=author, subscriber=user).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {"errors": "Вы не подписаны на данного пользователя!"},
                status=status.HTTP_400_BAD_REQUEST
            )
