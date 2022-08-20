from django.contrib import admin
from post.models import Post, Slider, Category, Comment, Galery


class GaleryItems(admin.TabularInline):
    model = Galery
    extra = 4
    max_num = 10


class PostAdmin(admin.ModelAdmin):
    inlines = [GaleryItems]
    list_display = ['title', 'category', 'create_time', 'slug', 'draft']
    list_filter = ['title', 'draft']
    search_fields = ['title', 'content']


admin.site.register(Post, PostAdmin)

admin.site.register(Slider)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)

admin.site.register(Galery)
