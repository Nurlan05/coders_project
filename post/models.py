from django.db import models
from post.helper import seo
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext_lazy as _
from accounts.models import MyUser

class Category(models.Model):
    title = models.CharField(max_length=1200, verbose_name=_("Category name"))
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


class Settings(models.Model):
    about_text = models.CharField(max_length=1500, verbose_name="Sayt haqqında(SEO mətni)")
    meta_keywords = models.CharField(max_length=1500, verbose_name="Meta Keywords", null=True, blank=True)
    site_title = models.CharField(max_length=1500, verbose_name="Saytın başlığı")
    email = models.CharField(max_length=1500, verbose_name="Email", null=True)
    number = models.CharField(max_length=1500, verbose_name="Nömrə", null=True)
    adress = models.CharField(max_length=1500, verbose_name="Ünvan", null=True)
    g_adress = models.CharField(max_length=1500, verbose_name="Google Map linki", null=True,blank=True)
    logo = models.FileField(verbose_name="Qara logo(163x38)", blank=True)
    dark_logo = models.FileField(verbose_name="Ağ logo(163x38)", blank=True, null=True)
    favicon = models.FileField(verbose_name="favicon(32x32)", blank=True, null=True)

    proloader_logo = models.FileField(verbose_name="Preloader logo(163x38)",help_text="Sayt açılanda yükənən logo", blank=True, null=True)
    footer_logo = models.FileField(verbose_name="Footer logo(163x38)",help_text="Saytın aşağısındakı logo", blank=True, null=True)
    facebook = models.CharField(max_length=1500, verbose_name="Facebook", blank=True)
    instagram = models.CharField(max_length=1500, verbose_name="İnstagram", blank=True)
    linkedin = models.CharField(max_length=1500, verbose_name="Linkedin", blank=True)
    youtube = models.CharField(max_length=1500, verbose_name="Youtube", blank=True)
    medium = models.CharField(max_length=1500, verbose_name="Medium", blank=True)
    google_business = models.CharField(max_length=1500, verbose_name="Google Business", blank=True, null=True)
    twitter = models.CharField(max_length=1500, verbose_name="Twitter", null=True, blank=True)
    slug = models.SlugField(editable=False, verbose_name="Slug")
    c_meta_title = models.CharField(max_length=1500, verbose_name="Əlaqə Meta title", null=True, blank=False)
    c_meta_keywords = models.CharField(max_length=1500, verbose_name="Əlaqə Meta keywords", null=True, blank=True)
    c_meta_description = models.TextField(max_length=160, verbose_name="Əlaqə Meta description", null=True,
                                          blank=False, help_text="Meta descriptionda max. 150 hərf ola bilər!")
    n_meta_title = models.CharField(max_length=1500, verbose_name="Xəbər Meta title", null=True, blank=False)
    n_meta_description = models.TextField(max_length=160, verbose_name="Xəbər Meta description", null=True,
                                          blank=False, help_text="Meta descriptionda max. 150 hərf ola bilər!")

    def __str__(self):
        return ('%s') % (self.site_title)

    class Meta:
        verbose_name = "Tənzimləmə"
        verbose_name_plural = "Tənzimləmələr"
        ordering = ['-id']

    def save(self, *args, **kwargs):
        self.slug = seo(self.site_title)
        super(Settings, self).save(*args, **kwargs)
