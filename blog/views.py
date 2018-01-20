from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
# Create your views here.
def index(request):
    #bringing posts from the model
    posts = Blog.objects.all()[:10]
    
    context = {
        'title':'Latest POSTS',
        'posts': posts
    }

    return render(request, 'blog/index.html', context)

def details(request, id):
    post = Blog.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'blog/details.html', context)