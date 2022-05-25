from django.urls import include, path
from rest_framework.routers import DefaultRouter

from ingredients import views

app_name = 'ingredients'

router = DefaultRouter()
router.register('', views.IngredientsViewSet, basename='ingredients')

urlpatterns = [
    path('', include(router.urls), name='api-ingredients'),
]
