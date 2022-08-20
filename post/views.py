from django.shortcuts import render, get_object_or_404, redirect
from post.models import Post, Slider, Category,Galery
from post.forms import CommentForm
from post.models import Comment

def index_view(request):

    context = {}

    context['post_list'] = Post.objects.filter(draft=True)
    context['category_list'] = Category.objects.all()

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
    obj = get_object_or_404(Post, slug=slug)
    context['obj'] = obj

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = obj
            comment.save()
            return redirect(obj.get_absolute_url())
    else:
        form = CommentForm()
        context['form'] = form

    context['form']=form
    context['comment_list']=Comment.objects.filter(post=obj).order_by('-id')
    context['galery_list']=Galery.objects.filter(post=obj).order_by('-id')
    return render(request, 'post/post_detail.html', context)


def category_detail(request, slug):
    context = {}
    obj = get_object_or_404(Category, slug=slug)
    context['post_list'] = obj.data.all()

    return render(request, 'post/category.html', context)
