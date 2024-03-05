from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import PostForm

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

def delete(request, title):
    post = get_object_or_404(BlogPost, title=title)
    context = {"post":post}
    if request.method == "POST":
        post.delete()
        messages.success(request, 'Blog post deleted successfully.')
        return redirect('home')
    return render(request, "delete.html", context)
    # return render(request, "home.html", context)

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_posts')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})