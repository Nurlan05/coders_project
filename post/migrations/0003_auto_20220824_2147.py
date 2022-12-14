# Generated by Django 2.2.16 on 2022-08-24 17:47

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='title_az',
            field=models.CharField(max_length=1200, null=True, verbose_name='Category name'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_en',
            field=models.CharField(max_length=1200, null=True, verbose_name='Category name'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_tr',
            field=models.CharField(max_length=1200, null=True, verbose_name='Category name'),
        ),
        migrations.AddField(
            model_name='post',
            name='content_az',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Post content'),
        ),
        migrations.AddField(
            model_name='post',
            name='content_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Post content'),
        ),
        migrations.AddField(
            model_name='post',
            name='content_tr',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Post content'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_az',
            field=models.CharField(help_text='Burda xeberin basligi yazilir', max_length=1500, null=True, verbose_name='Post title'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=models.CharField(help_text='Burda xeberin basligi yazilir', max_length=1500, null=True, verbose_name='Post title'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_tr',
            field=models.CharField(help_text='Burda xeberin basligi yazilir', max_length=1500, null=True, verbose_name='Post title'),
        ),
    ]
