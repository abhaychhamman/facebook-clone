# Generated by Django 4.0.5 on 2023-01-28 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createcontent', '0014_dopost_remove_post_comment_post_commentcounter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dopost',
            name='commentsUsername',
            field=models.CharField(default='', max_length=50),
        ),
    ]