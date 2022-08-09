from django.urls import path
from post.views import index_view, slider_view

urlpatterns = [
    path('slider/', index_view, name="index"),
    path('', slider_view, name="slider"),

]
