from datetime import date, timedelta
import datetime

import requests as requests
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from post.models import Post, Slider, Category, Galery,Comment,PostTrue
from post.forms import CommentForm, PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.decorators import api_view
from rest_framework.response import Response
from post.serializers import PostSerializer


def index_view(request):
    context = {}

    today = datetime.datetime.now()
    context['today'] = today
    around = date.today() - timedelta(days=15)
    around_b = date.today() + timedelta(days=25)
    context['post_list'] = Post.objects.filter(draft=True, create_time__gt=around, create_time__lt=around_b).order_by(
        '-create_time')
    # context['post_list'] = Post.objects.filter(draft=True).order_by('-id')

    return render(request, 'home/home.html', context)


def slider_view(request):
    context = {}
    context['slider_list'] = Slider.objects.all()

    return render(request, 'slider/slider.html', context)


def post_list_view(request):
    context = {}
    # post_list = Post.objects.filter(draft=True)
    # page = request.GET.get('page')
    # paginator = Paginator(post_list, 2)
    #
    # try:
    #     post_list=paginator.page(page)
    #
    # except PageNotAnInteger:
    #     post_list= paginator.page(1)
    # except EmptyPage:
    #
    #     post_list=paginator.page(paginator.num_pages)

    #
    # context['posts'] =post_list

    post_list = requests.get('http://localhost:8000/api/post-list').json()
    context['posts'] = post_list
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
            messages.error(request, 'Sizin şərhiniz uğurla əlavə olundu!')
            return redirect(obj.get_absolute_url())
    else:
        form = CommentForm()
        context['form'] = form
    context['post_list'] = Post.objects.filter(category=obj.category).exclude(pk=obj.id).order_by('-id')
    context['form'] = form
    context['comment_list'] = Comment.objects.filter(post=obj).order_by('-id')
    context['comment_count'] = Comment.objects.filter(post=obj).order_by('-id').count()
    context['galery_list'] = Galery.objects.filter(post=obj).order_by('-id')
    return render(request, 'post/post_detail.html', context)


def category_detail(request, slug):
    context = {}
    obj = get_object_or_404(Category, slug=slug)
    context['post_list'] = obj.data.all()

    return render(request, 'post/category.html', context)


def post_create(request):
    context = {}
    if not request.user.is_authenticated:
        return redirect('post:index')
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.author = request.user
            data.save()
            draft = form.cleaned_data.get('draft')
            if draft == True:
                PostTrue.objects.create(post=data,title=form.cleaned_data.get('title'))

            messages.success(request, 'Sizin postunuz uğurla əlavə olundu!')
            return redirect('post:post_create')


    else:
        form = PostForm()
        context['form'] = form
    context['form'] = form
    return render(request, 'form/post_create.html', context)


def post_update(request, slug):
    context = {}
    if not request.user.is_authenticated:
        return redirect("post:index")
    obj = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES or None, instance=obj)

        if form.is_valid():
            form.save()
            messages.success(request, 'Sizin postunuz uğurla yeniləndi!')
            return redirect(obj.get_absolute_url())
        else:
            context['form'] = form
    context["form"] = PostForm(instance=obj)

    return render(request, 'form/post_create.html', context)


def post_delete(request, slug):
    if not request.user.is_authenticated:
        return redirect("post:index")
    obj = get_object_or_404(Post, slug=slug)

    data = Post.objects.filter(slug=slug).last()
    # data.delete()
    data.draft = False
    data.save()
    return redirect(obj.get_absolute_url())


@api_view(['GET'])
def view_api(request):
    news = Post.objects.all()
    serializer = PostSerializer(news, many=True)
    return Response(serializer.data)
