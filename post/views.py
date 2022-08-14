from django.shortcuts import render, get_object_or_404, redirect
from post.models import Post, Slider, Category


def index_view(request):
    context = {}
    context['post_list'] = c = Post.objects.filter(draft=True)[:2]
    a = Post.objects.all().count()

    print(c)

    return render(request, 'home/home.html', context)


def slider_view(request):
    context = {}
    context['slider_list'] = Slider.objects.all()

    return render(request, 'slider/slider.html', context)


def post_list_view(request):
    context = {}
    context['post_list'] = Post.objects.filter(draft=True)
    return render(request, 'post/post_list.html', context)


def post_detail(request, slug):
    context = {}
    post = get_object_or_404(Post, slug=slug)
    context['obj'] = post

    return render(request, 'post/post_detail.html', context)

# def category_view(request,slug):
