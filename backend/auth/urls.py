from django.urls import path

from auth import views

app_name = 'auth'

urlpatterns = [
    path('token/login/', views.Login, name='login'),
    path('token/logout/', views.Logout, name='logout'),
]
