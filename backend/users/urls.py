from django.urls import include, path
# from rest_framework.routers import SimpleRouter

from users import views

app_name = 'users'

# router = SimpleRouter()
# router.register('', views.UserViewSet, basename='user')

urlpatterns = [
    # path('me/', views.UserViewSet.as_view('me'), name='current_user'),
    # path('set_password/', views.Test2, name='set_password'),
    path('subscriptions/', views.SubscriptionsView.as_view(), name='subscriptions'),
    path('<int:user_id>/subscribe/', views.SubscribeView.as_view(), name='subscribe'),
    # path('', include(router.urls)),
    # path('<int:user_id>/', views.Test3, name='user'),
]
