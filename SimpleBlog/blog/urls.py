from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("all-posts", views.all_posts, name="all_posts"),
    path("blog", views.all_posts, name="all_posts"),
    path("blog/<str:title>", views.blog, name="blog"),
    path("delete/<str:title>", views.delete, name="delete"),
]