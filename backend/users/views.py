from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users import serializers
from users.models import Subscription, User


class SubscriptionsApiView(APIView):
    """Возвращает список подписок текущего пользователя на других пользователей."""

    def get(self, request):
        user = request.user
        subscriptions = Subscription.objects.filter(subscriber=user)
        authors_list = [author.author.id for author in subscriptions]
        authors = User.objects.filter(id__in=authors_list)
        serializer = serializers.SubscriptionsSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubscribeApiView(APIView):
    """Добавляет либо удаляет подписку на данного пользователя."""

    def post(self, request, user_id):
        author = get_object_or_404(User, id=user_id)
        if author == request.user:
            return Response(
                {"errors": "Нельзя подписываться на самого себя!"},
                status=status.HTTP_400_BAD_REQUEST
            )
        if Subscription.objects.filter(author=author, subscriber=request.user).exists():
            return Response(
                {"errors": "Вы уже подписаны на данного пользователя."},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            new_subscribe = Subscription.objects.create(author=author, subscriber=request.user)
            new_subscribe.save()
            serializer = serializers.SubscriptionsSerializer(author)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, user_id):
        author = get_object_or_404(User, id=user_id)
        if author == request.user:
            return Response(
                {"errors": "Нельзя отписаться от себя!"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if Subscription.objects.filter(author=author, subscriber=request.user).exists():
            subscribe = Subscription.objects.get(author=author, subscriber=request.user)
            subscribe.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {"errors": "Вы не подписаны на данного пользователя!"},
                status=status.HTTP_400_BAD_REQUEST
            )
