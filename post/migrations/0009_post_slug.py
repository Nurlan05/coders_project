# Generated by Django 2.2.16 on 2022-08-12 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(editable=False, null=True, verbose_name='Slug'),
        ),
    ]