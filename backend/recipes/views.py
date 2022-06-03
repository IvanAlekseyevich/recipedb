from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from recipes import serializers
from recipes.models import FavoriteRecipe, Recipe, ShoppingCart


class RecipeViewSet(viewsets.ModelViewSet):
    """
    Возвращает список рецептов, либо конкретный рецепт,
    создает/изменяет/удаляет рецепт.
    """
    queryset = Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer
    # permission_classes = []
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('tags__slug',)


class FavoriteRecipeApiView(APIView):
    """Добавляет либо удаляет рецепт из избранного."""

    def post(self, request, recipe_id):
        user = request.user
        recipe = get_object_or_404(Recipe, id=recipe_id)
        if FavoriteRecipe.objects.filter(user=user, recipe=recipe).exists():
            return Response(
                {"errors": "Вы уже добавили рецепт в избранное."},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            new_favorite = FavoriteRecipe.objects.create(user=user, recipe=recipe)
            new_favorite.save()
            serializer = serializers.ShortRecipeSerializer(recipe)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, recipe_id):
        user = request.user
        recipe = get_object_or_404(Recipe, id=recipe_id)
        if FavoriteRecipe.objects.filter(user=user, recipe=recipe).exists():
            old_favorite = FavoriteRecipe.objects.get(user=user, recipe=recipe)
            old_favorite.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {"errors": "У вас нету данного рецепта в избранном."},
                status=status.HTTP_400_BAD_REQUEST
            )


class ShoppingCartApiView(APIView):
    """Добавляет либо удаляет рецепт из списка покупок."""

    def post(self, request, recipe_id):
        user = request.user
        recipe = get_object_or_404(Recipe, id=recipe_id)
        if ShoppingCart.objects.filter(user=user, recipe=recipe).exists():
            return Response(
                {"errors": "Вы уже добавили рецепт в список покупок."},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            new_shoping = ShoppingCart.objects.create(user=user, recipe=recipe)
            new_shoping.save()
            serializer = serializers.ShortRecipeSerializer(recipe)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, recipe_id):
        user = request.user
        recipe = get_object_or_404(Recipe, id=recipe_id)
        if ShoppingCart.objects.filter(user=user, recipe=recipe).exists():
            old_shoping = ShoppingCart.objects.get(user=user, recipe=recipe)
            old_shoping.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {"errors": "У вас нету данного рецепта в списке покупок."},
                status=status.HTTP_400_BAD_REQUEST
            )
