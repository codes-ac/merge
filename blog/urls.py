from django.urls import path
from . import views
from django.contrib import admin    

urlpatterns = [
    path('postComment', views.postComment, name="postComment"),
    path('', views.blogHome, name="blogHome"),
    path('<str:slug>', views.blogPost, name="blogPost"),
    path('user/postBlog/', views.postBlog, name="postBlog"),
] 