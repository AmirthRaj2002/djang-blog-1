from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from blog.models import Post, Comment

from django.views.generic.detail import DetailView

def index(request):
    context_dict = {"posts": Post.objects.all()}
    return render(request, "blog/home.html", context=context_dict)

def blog_post(request, index):
    post = Post.objects.filter(id=index).first()
    context_dict = {
        "post": post,
        "comments": Comment.objects.filter(post=post)
    }
    
    return render(request, "blog/post.html", context=context_dict)