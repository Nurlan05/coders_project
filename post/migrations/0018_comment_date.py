# Generated by Django 2.2.16 on 2022-08-19 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0017_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date'),
        ),
    ]