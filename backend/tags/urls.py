from django.urls import path

from tags.views import AllTagsView, TagView

app_name = 'tags'

urlpatterns = [
    path('', AllTagsView.as_view(), name='all_tags'),
    path('<int:tag_id>/', TagView.as_view(), name='tag'),
]
