from django.urls import path

from tags import views

app_name = 'tags'

urlpatterns = [
    path('', views.Test1, name='all_tags'),
    path('<int:tag_id>/', views.Test2, name='tag'),
]
