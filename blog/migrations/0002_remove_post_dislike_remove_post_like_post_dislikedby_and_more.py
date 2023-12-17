# Generated by Django 5.0 on 2023-12-17 12:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='post',
            name='like',
        ),
        migrations.AddField(
            model_name='post',
            name='dislikedBy',
            field=models.ManyToManyField(related_name='dislikedBy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='likedBy',
            field=models.ManyToManyField(related_name='likedBy', to=settings.AUTH_USER_MODEL),
        ),
    ]