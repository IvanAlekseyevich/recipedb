from django.urls import include, path
from rest_framework.routers import DefaultRouter

from recipes import views

app_name = 'recipes'

router = DefaultRouter()
router.register('', views.RecipeViewSet, basename='recipe')

urlpatterns = [

    path('<int:recipe_id>/shopping_cart/', views.ShoppingCartApiView.as_view(), name='shopping_cart'),
    path('<int:recipe_id>/favorite/', views.FavoriteRecipeApiView.as_view(), name='favorite_recipe'),
    path('download_shopping_cart/', views.DownloadShopping.as_view(), name='shopping_list'),
    path('', include(router.urls)),
]
