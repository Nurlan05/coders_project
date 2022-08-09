from django.shortcuts import render
from post.models import Post, Slider


def index_view(request):
    context = {}
    context['post_list'] = Post.objects.filter(draft=True)

    return render(request, 'base.html', context)


def slider_view(request):
    context = {}
    context['slider_list'] = Slider.objects.all()

    return render(request, 'slider/slider.html', context)
