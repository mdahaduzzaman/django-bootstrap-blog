# Generated by Django 5.0 on 2023-12-30 16:18

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_dislike_remove_post_like_post_dislikedby_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
