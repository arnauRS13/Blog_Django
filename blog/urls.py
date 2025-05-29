from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.post_list, name='post-list'),
    path('posts/<slug:slug>/', views.post_detail, name='posts-detail-page'),
    path('authors/', views.authors_list, name='authors-list'),
    path('authors/<int:author_id>/', views.author_detail, name='author-detail'),
    path('tags/', views.tag_list, name='tags-list'),
    path('tags/<str:tag>/', views.tag_post_list, name='tag-post-list'),
]
