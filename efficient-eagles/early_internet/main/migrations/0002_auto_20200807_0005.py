# Generated by Django 3.0.8 on 2020-08-07 00:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="downvoted_by",
            field=models.ManyToManyField(
                related_name="comment_downvoted_by", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="thread_level",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="comment",
            name="upvoted_by",
            field=models.ManyToManyField(
                related_name="comment_upvoted_by", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="downvoted_by",
            field=models.ManyToManyField(
                related_name="downvoted_by", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="upvoted_by",
            field=models.ManyToManyField(
                related_name="upvoted_by", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]