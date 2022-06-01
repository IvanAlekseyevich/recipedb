from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users import serializers
from users.models import Subscription, User


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     Возвращает всех пользователей, либо конкретного
#     пользователя, создает/изменяет/удаляет пользователей.
#     """
#     queryset = User.objects.all()
#     permission_classes = []
#
#     # def get_queryset(self):
#     #     is_subscribed = Subscription.objects.filter(subscriber=self.request.user).exist()
#     #     queryset = User.objects.annotate(is_subscribed=is_subscribed)
#     #     return queryset
#     def me(self):
#         user = self.request.user
#         queryset = User.objects.get(pk=user.pk)
#         return queryset
#
#     def get_serializer_class(self):
#         if self.action == 'create':
#             return serializers.CustomUserCreateSerializer
#
#         return serializers.CustomUserSerializer

class SubscriptionsApiView(APIView):
    def get(self, request):
        user = request.user
        subscriptions = Subscription.objects.filter(subscriber=user)
        serializer = serializers.CustomUserSerializer(subscriptions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubscribeApiView(APIView):
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
            return Response(serializers.SubscriptionsSerializer)

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
            return Response({''}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {"errors": "Вы не подписаны на данного пользователя!"},
                status=status.HTTP_400_BAD_REQUEST
            )


class Test2():
    pass


class Test3():
    pass


class Test4():
    pass
