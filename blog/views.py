from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from blog.models import Post, MetaField


def blog(request):
    blogs = Post.objects.all()
    meta = MetaField.objects.all()
    # pagnation = Paginator(blogs, 5)
    return render(request, 'blog.html', {'blogs': blogs, 'meta': meta})


def blog_post(request, post_id):
    blog = Post.objects.get(pk=post_id)
    meta = MetaField.objects.filter(posts__id=post_id)
    return render(request, 'blog_post.html', {"blog": blog, "meta":meta})

def coding(request):
    return render(request, 'coding_zero.html')