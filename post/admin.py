from django.contrib import admin
from post.models import Post,Slider


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_time','slug' ,'draft']
    list_filter = ['title', 'draft']
    search_fields = ['title', 'content']


admin.site.register(Post, PostAdmin)

admin.site.register(Slider)