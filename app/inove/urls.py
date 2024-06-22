# inove/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.list_posts, name='list_posts'),
    path('posts/<int:post_id>/', views.view_post, name='view_post'),
    path('create_post/', views.create_post, name='create_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('users/', views.list_users, name='list_users'),
    path('users/<int:user_id>/', views.view_user, name='view_user'),

]
