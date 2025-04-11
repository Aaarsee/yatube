from django.urls import path

from . import views
app_name = 'posts'
urlpatterns = [
    path('', views.index, name='main'),
    path('group/<slug:slug>/', views.group_posts, name='group_posts'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('new/', views.new_post, name='new_post')
    ]
