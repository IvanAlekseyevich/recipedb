from django.urls import include, path
from rest_framework.routers import DefaultRouter

from tags import views

app_name = 'tags'

router = DefaultRouter()
router.register('', views.TagViewSet, basename='tags')

urlpatterns = [
    path('', include(router.urls), name='api-tags'),
]
