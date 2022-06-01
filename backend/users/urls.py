from django.contrib.auth import get_user_model
from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import DefaultRouter

from users import views

app_name = 'users'

router = DefaultRouter()
router.register("", UserViewSet)

User = get_user_model()

urlpatterns = [

    path('subscriptions/', views.SubscriptionsApiView.as_view(), name='subscriptions'),
    path('<int:user_id>/subscribe/', views.SubscribeApiView.as_view(), name='subscribe'),
    path('', include(router.urls)),
]
