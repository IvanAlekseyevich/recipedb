from django.shortcuts import HttpResponse, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from recipes import serializers
from recipes.models import FavoriteRecipe, Recipe, RecipeIngredient, ShoppingCart
from recipes.permissions import IsAuthorOrStaffOrReadOnly


class RecipeViewSet(viewsets.ModelViewSet):
    """
    Возвращает список рецептов, либо конкретный рецепт,
    создает/изменяет/удаляет рецепт.
    """
    queryset = Recipe.objects.all()
    permission_classes = [IsAuthorOrStaffOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('tags__slug',)

    def get_serializer_class(self):
        if self.action in ('create', 'update'):
            return serializers.RecipeCreateUpdateSerializer
        return serializers.RecipeListSerializer


class FavoriteRecipeApiView(APIView):
    """Добавляет либо удаляет рецепт из избранного."""
    permission_classes = [permissions.IsAuthenticated]

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
    permission_classes = [permissions.IsAuthenticated]

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


class DownloadShopping(APIView):
    """Выгружает ингридиенты из списка покупок."""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        recipe_list = RecipeIngredient.objects.filter(recipe__shopping__user=user)
        ingrid_amount = {}
        for recipe in recipe_list:
            name = recipe.ingredient.name
            measurement_unit = recipe.ingredient.measurement_unit
            amount = recipe.amount
            if f'{name} ({measurement_unit})' in ingrid_amount:
                ingrid_amount[f'{name} ({measurement_unit})'] += amount
            else:
                ingrid_amount[f'{name} ({measurement_unit})'] = amount
        shopping_list = []
        for ingridient, amount in ingrid_amount.items():
            shopping_list.append(f'{ingridient} - {amount}\n')
        shopping_list.sort()
        response = HttpResponse(shopping_list, 'Content-Type: text/plain')
        response['Content-Disposition'] = (
            'attachment;' 'filename="shopping_list.txt"'
        )
        return response
