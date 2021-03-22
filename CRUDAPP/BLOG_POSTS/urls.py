from django.urls import path

from . import views

app_name = "BLOG_POSTS"
urlpatterns = [
    path('', views.post_list, name='list'),
    path('new/', views.post_create, name='creater'),
    path('edit/<int:post_id>/', views.post_update, name='edit'),
    path('delete/<int:post_id>/', views.post_del, name='delete'),
]