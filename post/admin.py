from django.contrib import admin
from post.models import Post, Slider, Category, Comment, Galery, Settings
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from post.send_mail import send_subscriber_mail


def publish_post(modeladmin, request, queryset):
    queryset.update(draft=True)


publish_post.short_description = "Seçilmiş xəbərləri yayınla"


def draft_post(modeladmin, request, queryset):
    queryset.update(draft=False)


draft_post.short_description = "Seçilən xəbərləri qaralama olaraq qeyd et"


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
    actions = [publish_post, draft_post]

    def save_model(self, request, obj, form, change):
        post = obj
        title = obj.title
        content = obj.content
        link = obj.get_absolute_url()
        current_site = get_current_site(request)
        if obj.draft == True:
            send_subscriber_mail(title, content, link,current_site )


admin.site.register(Post, PostAdmin)

admin.site.register(Slider)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    exclude = ['title', ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)

admin.site.register(Galery)


class SettinsgAdmin(admin.ModelAdmin):
    list_display = ['site_title', ]


admin.site.register(Settings, SettinsgAdmin)
