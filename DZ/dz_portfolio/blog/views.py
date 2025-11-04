from django.shortcuts import render
from .models import Blog


def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blogs.html', {'blogs': blogs})


# def detail(request, blog_id):
#     return render(request, 'blog/details.html', {'id': blog_id})
