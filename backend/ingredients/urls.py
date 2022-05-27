from django.urls import path

from ingredients.views import AllIngredientsView, IngredientView

app_name = 'ingredients'

urlpatterns = [
    path('', AllIngredientsView.as_view(), name='all_ingredients'),
    path('<int:ingredients_id>/', IngredientView.as_view(), name='ingredient'),
]
