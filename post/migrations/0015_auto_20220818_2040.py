# Generated by Django 2.2.16 on 2022-08-18 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_auto_20220818_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True, unique=True, verbose_name='Slug'),
        ),
    ]
