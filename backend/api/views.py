from api import serializers
from api.filters import RecipeFilter
from api.permissions import (IsAuthorOrStaffOrReadOnlyPermission,
                             ReadOnlyPermission)
from django.db.models import Sum
from django.shortcuts import HttpResponse, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from recipes.models import (FavoriteRecipe, Ingredient, Recipe,
                            RecipeIngredient, ShoppingCart, Tag)
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import RecipeMinifiedSerializer


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    """Возвращает список ингредиентов с возможностью поиска по имени."""
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer
    permission_classes = [ReadOnlyPermission]
    pagination_class = None

    def get_queryset(self):
        queryset = Ingredient.objects.all()
        ingridient = self.request.query_params.get('name')
        if ingridient is not None:
            return queryset.filter(name__istartswith=ingridient)
        return queryset


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    """Возвращает список тегов."""
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer
    permission_classes = [ReadOnlyPermission]
    pagination_class = None


class RecipeViewSet(viewsets.ModelViewSet):
    """
    Возвращает список рецептов, либо конкретный рецепт,
    создает/изменяет/удаляет рецепт.
    """
    queryset = Recipe.objects.all()
    permission_classes = [IsAuthorOrStaffOrReadOnlyPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_class = RecipeFilter

    def get_serializer_class(self):
        if self.action in ('create', 'update'):
            return serializers.RecipeCreateUpdateSerializer
        return serializers.RecipeListSerializer

    def get_queryset(self):
        queryset = Recipe.objects.all()
        shopping = self.request.query_params.get('is_in_shopping_cart')
        favorite = self.request.query_params.get('is_favorited')
        if shopping is not None:
            return queryset.filter(shopping__user=self.request.user)
        if favorite is not None:
            return queryset.filter(favorite__user=self.request.user)
        return queryset


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
        FavoriteRecipe.objects.create(user=user, recipe=recipe)
        serializer = RecipeMinifiedSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, recipe_id):
        user = request.user
        recipe = get_object_or_404(Recipe, id=recipe_id)
        if FavoriteRecipe.objects.filter(user=user, recipe=recipe).exists():
            FavoriteRecipe.objects.get(user=user, recipe=recipe).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"errors": "У вас нету данного рецепта в избранном."}, status=status.HTTP_400_BAD_REQUEST)


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
        ShoppingCart.objects.create(user=user, recipe=recipe)
        serializer = RecipeMinifiedSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, recipe_id):
        user = request.user
        recipe = get_object_or_404(Recipe, id=recipe_id)
        if ShoppingCart.objects.filter(user=user, recipe=recipe).exists():
            ShoppingCart.objects.get(user=user, recipe=recipe).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"errors": "У вас нету данного рецепта в списке покупок."}, status=status.HTTP_400_BAD_REQUEST)


class DownloadShopping(APIView):
    """Выгружает ингридиенты из списка покупок в shopping_list.txt."""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        recipe_list = RecipeIngredient.objects.filter(
            recipe__shopping__user=user
        ).values(
            'ingredient__name', 'ingredient__measurement_unit'
        ).annotate(amount=Sum('amount'))
        shopping_list = []
        for ingredient in recipe_list:
            name = ingredient['ingredient__name']
            measurement_unit = ingredient['ingredient__measurement_unit']
            amount = ingredient['amount']
            shopping_list.append(f'{name} ({measurement_unit}) - {amount}\n')
        response = HttpResponse(shopping_list, 'Content-Type: text/plain')
        response['Content-Disposition'] = ('attachment;' 'filename="shopping_list.txt"')
        return response
