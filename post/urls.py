from django.urls import path
from post.views import index_view, slider_view,post_detail,post_list_view

app_name="post"

urlpatterns = [
    path('', index_view, name="index"),
    path('slaydlar/', slider_view, name="slider"),
    path('post/<slug>/', post_detail, name="detail_view"),
    path('post-list/',post_list_view,name="post-list")

]
