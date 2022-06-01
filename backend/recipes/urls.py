from django.urls import include, path
from rest_framework.routers import SimpleRouter

from recipes import views

app_name = 'recipes'

router = SimpleRouter()
router.register('', views.RecipeViewSet, basename='recipe')

urlpatterns = [

    path('<int:recipe_id>/shopping_cart/', views.ShoppingCartApiView.as_view(), name='add_shopping'),
    path('<int:recipe_id>/favorite/', views.FavoriteRecipeApiView.as_view(), name='add_favorite'),
    #path('download_shopping_cart/', views.Test3, name='shopping_list'),
    path('', include(router.urls)),
]
