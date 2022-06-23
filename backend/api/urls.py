from api import views
from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import DefaultRouter
from users.views import SubscribeApiView, SubscriptionsApiView

app_name = 'api'

router = DefaultRouter()
router.register('ingredients', views.IngredientViewSet, basename='ingredients')
router.register('tags', views.TagViewSet, basename='tags')
router.register('recipes', views.RecipeViewSet, basename='recipes')
router.register('users', UserViewSet)

urlpatterns = [
    path('recipes/<int:recipe_id>/shopping_cart/', views.ShoppingCartApiView.as_view(), name='shopping_cart'),
    path('recipes/<int:recipe_id>/favorite/', views.FavoriteRecipeApiView.as_view(), name='favorite_recipe'),
    path('recipes/download_shopping_cart/', views.DownloadShopping.as_view(), name='shopping_list'),
    path('users/subscriptions/', SubscriptionsApiView.as_view(), name='subscriptions'),
    path('users/<int:user_id>/subscribe/', SubscribeApiView.as_view(), name='subscribe'),
    path('', include(router.urls)),
]
