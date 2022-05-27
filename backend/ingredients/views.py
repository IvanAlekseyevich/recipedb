from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ingredients.models import Ingredient
from ingredients.serializers import IngredientSerializer


class AllIngredientsView(APIView):
    """Возвращает все ингридиенты, создает ингридиенты."""

    # permission_classes = []
    def get(self, request):
        ingredient = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredient, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IngredientView(APIView):
    """Возвращает конкретный ингридиент, изменяет и удаляет его."""

    # permission_classes = []
    def get(self, request, ingredients_id):
        current_ingredient = get_object_or_404(Ingredient, id=ingredients_id)
        serializer = IngredientSerializer(current_ingredient)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, ingredients_id):
        current_ingredient = get_object_or_404(Ingredient, id=ingredients_id)
        serializer = IngredientSerializer(
            current_ingredient,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, ingredients_id):
        current_ingredient = get_object_or_404(Ingredient, id=ingredients_id)
        current_ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
