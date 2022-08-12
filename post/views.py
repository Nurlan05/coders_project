from django.shortcuts import render
from post.models import Post, Slider


def index_view(request):
    context = {}
    context['post_list'] = Post.objects.filter(draft=True)

    return render(request, 'home/home.html', context)


def slider_view(request):
    context = {}
    context['slider_list'] = Slider.objects.all()

    return render(request, 'slider/slider.html', context)

def post_detail(request,slug):
    context={}

    context['obj']=Post.objects.get(slug=slug)

    return render(request,'post/post_detail.html',context)
