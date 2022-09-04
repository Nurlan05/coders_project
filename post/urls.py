from django.urls import path,include
from post.views import index_view, slider_view,post_detail,post_list_view,category_detail,post_create,post_update,post_delete

app_name="post"

urlpatterns = [
    path('', index_view, name="index"),
    path('slaydlar/', slider_view, name="slider"),
    path('post-list/',post_list_view,name="post-list"),
    path('post/create/', post_create, name="post_create"),
    path('post/<slug>/', post_detail, name="post_detail"),
    path('category/<slug>/', category_detail, name="category_detail"),

    path('post/update/<slug>/', post_update, name="post_update"),
    path('post/delete/<slug>/', post_delete, name="post_delete"),


]
