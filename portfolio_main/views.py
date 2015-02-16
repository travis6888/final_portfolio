from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def blog(request):
    return render(request, 'blog.html')


def blog_post(request):
    return render(request, 'blog_post.html')


def about(request):
    return render(request, 'about.html')


def resume(request):
    return render(request, 'resume.html')