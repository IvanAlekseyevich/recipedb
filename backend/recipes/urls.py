from django.urls import path

from recipes import views

app_name = 'recipes'

urlpatterns = [
    path('', views.Test1, name='all_recipes'),
    path('<int:recipe_id>/', views.Test2, name='recipe'),
    path('<int:recipe_id>/shopping_cart/', views.Test3, name='add_shopping'),
    path('<int:recipe_id>/favorite/', views.Test4, name='add_favorite'),
    path('download_shopping_cart/', views.Test5, name='shopping_list'),
]
