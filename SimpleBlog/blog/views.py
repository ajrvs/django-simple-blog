from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import BlogPost

# Create your views here.
def home(request):
    posts = BlogPost.objects.all()
    context = {"posts":posts}
    return render(request, "home.html", context)

def all_posts(request):
    posts = BlogPost.objects.all()
    context = {"posts":posts}
    return render(request, "all_posts.html", context)

def blog(request, title):
    post = get_object_or_404(BlogPost, title=title)
    context = {"post":post}
    return render(request, "blog.html", context)