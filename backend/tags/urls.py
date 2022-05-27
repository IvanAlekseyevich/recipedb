from django.urls import include, path
from rest_framework.routers import SimpleRouter

from tags.views import TagViewSet

app_name = 'tags'

router = SimpleRouter()
router.register('', TagViewSet, basename='tag')

urlpatterns = [
    path('', include(router.urls)),
]
