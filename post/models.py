from django.db import models
from post.helper import seo
from django.urls import reverse
from ckeditor.fields import RichTextField

from accounts.models import MyUser

class Category(models.Model):
    title = models.CharField(max_length=1200, verbose_name="Category name")
    image = models.ImageField(verbose_name="Category image", upload_to="category", blank=True)
    slug = models.SlugField(editable=False, verbose_name="Slug", null=True, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)
        self.slug = seo(self.title)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post:category_detail', kwargs={'slug': self.slug})


class Post(models.Model):
    author=models.ForeignKey(MyUser,related_name="user",on_delete=models.CASCADE,null=True,verbose_name="User")
    category = models.ForeignKey(Category, related_name="data", verbose_name="Category", null=True,
                                 on_delete=models.CASCADE)
    title = models.CharField(max_length=1500, verbose_name="Post title", help_text="Burda xeberin basligi yazilir")
    preview_count = models.IntegerField(verbose_name="Preview count", default=10, null=True)
    content = RichTextField(verbose_name="Post content", blank=True)
    create_time = models.DateTimeField(verbose_name="Post date", null=True, blank=True)
    image = models.ImageField(verbose_name="Shekil elave et", null=True, upload_to='post')
    draft = models.BooleanField(default=True, verbose_name="Saytda yayimlansin?")
    slug = models.SlugField(editable=False, verbose_name="Slug", null=True, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Xeber"
        verbose_name_plural = "Xeberler"

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        self.slug = seo(self.title + "-" + str(self.id))
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post:post_detail', kwargs={'slug': self.slug})


class Galery(models.Model):
    post = models.ForeignKey(Post, related_name="galery_post", verbose_name="Post", on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Image", upload_to='post/galery')

    def __str__(self):
        return "image#" + str(self.id)

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Galery images"
        ordering = ["-id"]


class Slider(models.Model):
    title = models.CharField(max_length=1500, verbose_name="Post title", help_text="Burda xeberin basligi yazilir")
    content = models.TextField(verbose_name="Post content", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Slayd"
        verbose_name_plural = "Slaydlar"


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comment_post", verbose_name="Post", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, verbose_name="Date", null=True)
    content = models.TextField(verbose_name="Comment")

    def __str__(self):
        return self.post.title + "-" + str(self.id)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
