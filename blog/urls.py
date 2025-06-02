from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'),
    path('post/<slug:slug>/edit/', views.edit_post, name='edit_post'),
    path('post/<slug:slug>/delete/', views.delete_post, name='delete_post'),
    path('my-posts/', views.my_posts, name='my_posts'),
    path('post/<slug:slug>/comment/', views.add_comment, name='add_comment'),
    path('post/<slug:slug>/like/', views.toggle_like, name='toggle_like'),
    path('search/', views.search_posts, name='search'),
    path('tag/<slug:tag_slug>/', views.tag_posts, name='tag_posts'),
    path('category/<slug:slug>/', views.category_posts, name='category_posts'),
]
