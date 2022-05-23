from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('me/', views.Test1, name='current_user'),
    path('set_password/', views.Test2, name='set_password'),
    path('subscriptions/', views.Test3, name='subscriptions'),
    path('<int:user_id>/', views.Test3, name='user'),
    path('<int:user_id>/subscribe/', views.Test4, name='subscribe'),
]
