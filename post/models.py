from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=1500, verbose_name="Post title", help_text="Burda xeberin basligi yazilir")
    content = models.TextField(verbose_name="Post content", blank=True)
    create_time = models.DateTimeField(verbose_name="Post date", null=True, blank=True)
    image=models.ImageField(verbose_name="Shekil elave et",null=True,upload_to='post')
    draft = models.BooleanField(default=True, verbose_name="Saytda yayimlansin?")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Xeber"
        verbose_name_plural = "Xeberler"


class Slider(models.Model):
    title = models.CharField(max_length=1500, verbose_name="Post title", help_text="Burda xeberin basligi yazilir")
    content = models.TextField(verbose_name="Post content", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Slayd"
        verbose_name_plural = "Slaydlar"

