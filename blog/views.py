from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def apt1(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/apt1.html', context)


def apt2(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/apt2.html', context)


def apt3(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/apt3.html', context)


def apt4(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/apt4.html', context)


def landlord(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/landlord.html', context)
