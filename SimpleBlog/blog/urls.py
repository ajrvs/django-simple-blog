from django.urls import path
from . import views, models

urlpatterns = [
    path("", views.home, name="home"),
    path("all-posts", views.all_posts, name="all_posts"),
    path("blog", views.all_posts, name="all_posts"),
    path("blog/<str:title>", views.blog, name="blog"),
    path("create/", views.create_post, name="create_post"),
    path("edit/<str:title>", views.update_post, name="update_post"),
    path("delete/<str:title>", views.delete, name="delete")
]
