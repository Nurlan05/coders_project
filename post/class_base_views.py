from django.views import generic
from django.views.generic import ListView, DetailView
from post.models import Post


class PostListView(ListView):
    model = Post
    template_name = "post/class_post_list.html"

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['post_list']=Post.objects.filter(draft=True)



        return context
