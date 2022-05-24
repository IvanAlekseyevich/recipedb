from django.urls import path

from ingredients import views

app_name = 'ingredients'

urlpatterns = [
    path('', views.Test1, name='all_ingredients'),
    path('<int:ingredients_id>/', views.Test2, name='ingredient'),
]
