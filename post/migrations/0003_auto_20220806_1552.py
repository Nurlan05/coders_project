# Generated by Django 2.2.16 on 2022-08-06 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20220806_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Post date'),
        ),
    ]
