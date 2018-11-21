from django.urls import path
from . import views
# from .views import PostListView
############## Feeds ################
from .feeds import LatestPostsFeed
######################################



app_name = 'blog'


urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('tag/<slug:tag_slug>/',views.post_list, name='post_list_by_tag'),
    # path('', PostListView.as_view(),name='post_list'),
    path('<slug:post>/',views.post_detail , name='post_detail'),
    path('<int:id>/share/',views.post_share, name='post_share'),
    path('feed/', LatestPostsFeed(), name='post_feed'), # Feeds
    path('search/', views.post_search, name='post_search'),
]



   # <int:year>/<int:month>/<int:day>/
