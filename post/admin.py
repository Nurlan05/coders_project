from django.contrib import admin
from post.models import Post, Slider, Category, Comment, Galery
from django.contrib.auth import get_user_model


def publish_post(modeladmin, request, queryset):
    queryset.update(draft=True)
publish_post.short_description="Seçilmiş xəbərləri yayınla"

def draft_post(modeladmin,request,queryset):
    queryset.update(draft=False)
draft_post.short_description="Seçilən xəbərləri qaralama olaraq qeyd et"



class GaleryItems(admin.TabularInline):
    model = Galery
    extra = 4
    max_num = 10


class PostAdmin(admin.ModelAdmin):
    inlines = [GaleryItems]
    list_display = ['title', 'category', 'create_time', 'slug', 'draft']
    list_filter = ['title', 'draft']
    exclude = ['title', 'content']
    search_fields = ['title', 'content']
    actions = [publish_post,draft_post]


admin.site.register(Post, PostAdmin)

admin.site.register(Slider)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    exclude = ['title', ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)

admin.site.register(Galery)
