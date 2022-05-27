from django.urls import include, path
from rest_framework.routers import SimpleRouter

from ingredients.views import IngredientViewSet

app_name = 'ingredients'

router = SimpleRouter()
router.register('', IngredientViewSet, basename='ingredient')

urlpatterns = [
    path('', include(router.urls)),
]
